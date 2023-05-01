# Generated by Django 4.2 on 2023-05-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='long_url',
            field=models.URLField(max_length=800, verbose_name='Длинная ссылка'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='short_url',
            field=models.CharField(blank=True, max_length=15, unique=True, verbose_name='Короткая ссылка'),
        ),
    ]
