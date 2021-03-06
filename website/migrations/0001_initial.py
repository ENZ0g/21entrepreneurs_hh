# Generated by Django 3.0.8 on 2020-07-16 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartupProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('contact_name', models.CharField(max_length=50, verbose_name='Контактное лицо')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.TextField(verbose_name='Кого хотим видеть в команде')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.StartupProject', verbose_name='Название проекта')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack', models.CharField(blank=True, max_length=30)),
                ('telegram', models.CharField(blank=True, max_length=30)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.StartupProject', verbose_name='Название проекта')),
            ],
        ),
    ]
