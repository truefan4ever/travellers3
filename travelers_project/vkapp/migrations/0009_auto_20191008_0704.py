# Generated by Django 2.2.5 on 2019-10-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkapp', '0008_auto_20191003_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
