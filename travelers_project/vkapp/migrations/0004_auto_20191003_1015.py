# Generated by Django 2.2.5 on 2019-10-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkapp', '0003_auto_20191003_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album_id',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
