# Generated by Django 2.2.5 on 2019-10-07 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0009_auto_20191007_1351'),
        ('traces', '0007_remove_routebycities_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitiesRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.City')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traces.RouteByCities')),
            ],
        ),
        migrations.AddField(
            model_name='routebycities',
            name='cities',
            field=models.ManyToManyField(blank=True, through='traces.CitiesRelationship', to='geography.City'),
        ),
    ]
