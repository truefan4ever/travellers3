# Generated by Django 2.2.5 on 2019-09-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0004_auto_20190926_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='sight',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='photo/sights/', verbose_name='Фотография достопримечательности'),
        ),
    ]
