# Generated by Django 3.0.8 on 2020-07-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200716_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupproject',
            name='slack',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='startupproject',
            name='telegram',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
