# Generated by Django 2.2.5 on 2019-10-07 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traces', '0006_auto_20191004_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routebycities',
            name='cities',
        ),
    ]
