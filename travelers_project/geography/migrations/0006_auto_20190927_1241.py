# Generated by Django 2.2.5 on 2019-09-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0005_sight_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='show_on_mainmap',
            field=models.BooleanField(default=True, verbose_name='Показывать на главной карте'),
        ),
    ]