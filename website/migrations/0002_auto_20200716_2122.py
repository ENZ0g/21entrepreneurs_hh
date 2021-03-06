# Generated by Django 3.0.8 on 2020-07-16 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='website.StartupProject', verbose_name='Название проекта'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='website.StartupProject', verbose_name='Название проекта'),
        ),
    ]
