# Generated by Django 4.2.4 on 2023-08-11 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания'),
        ),
    ]