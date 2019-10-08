# Generated by Django 2.2.5 on 2019-10-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traces', '0008_auto_20191007_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routebycities',
            name='cities',
            field=models.ManyToManyField(through='traces.CitiesRelationship', to='geography.City'),
        ),
    ]
