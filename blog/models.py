from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview_image = models.ImageField(upload_to='blog/', verbose_name='Превью', null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


