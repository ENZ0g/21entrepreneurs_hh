# Generated by Django 3.0.8 on 2020-08-01 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200721_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='create_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='lifetime',
            field=models.SmallIntegerField(default=1, verbose_name='Время жизни записи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startupproject',
            name='create_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startupproject',
            name='lifetime',
            field=models.SmallIntegerField(default=1, verbose_name='Время жизни записи'),
            preserve_default=False,
        ),
    ]
