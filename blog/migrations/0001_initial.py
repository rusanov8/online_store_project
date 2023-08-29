# Generated by Django 4.2.4 on 2023-08-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью')),
                ('publication_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]