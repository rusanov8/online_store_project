# Generated by Django 4.2.4 on 2023-09-04 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='верифицирован'),
        ),
    ]
