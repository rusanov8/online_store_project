from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            subject = 'Поздравляем с достижением 100 просмотров!'
            message = 'Ваша статья достигла 100 просмотров. Поздравляем!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['russsssanov@yandex.ru']

            send_mail(subject, message, from_email, recipient_list)

        return self.object



class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview_image', )
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview_image',)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')




