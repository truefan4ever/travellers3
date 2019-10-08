# Generated by Django 2.2.5 on 2019-10-07 13:51

from django.db import migrations, models
import geography.models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0008_merge_20191007_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=geography.models.image_city, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='region',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=geography.models.image_region, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=geography.models.image_sight, verbose_name='Фотография достопримечательности'),
        ),
        migrations.AlterField(
            model_name='sightphoto',
            name='file',
            field=models.ImageField(default='', upload_to=geography.models.image_sight, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='sightphoto',
            name='posted',
            field=models.BooleanField(default=True),
        ),
    ]
