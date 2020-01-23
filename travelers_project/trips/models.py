from django.db import models
from traces.models import RouteByCities, RouteBySights
from django.contrib.auth.models import User


class Traveler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateTimeField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Путешественник'
        verbose_name_plural = 'Путешественники'


class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название путешествия')
    start_date = models.DateTimeField(verbose_name='Дата начала путешествия')
    end_date = models.DateTimeField(verbose_name='Дата окончания путешествия')
    description = models.TextField(default='', verbose_name='Описание путешествия')
    traveler = models.ManyToManyField(Traveler, related_name='trip_traveler', verbose_name='Путешественники')
    route_by_sights = models.ForeignKey(
        RouteBySights,
        on_delete=models.DO_NOTHING,
        related_name='trip_route_sight',
        blank=True,
        null=True,
        verbose_name='Путешествие по маршрутам достопримечательностей')
    route_by_cities = models.ForeignKey(
        RouteByCities,
        on_delete=models.DO_NOTHING,
        related_name='trip_route_city',
        blank=True,
        null=True,
        verbose_name='Путешествие по маршрутам городов')

    class Meta:
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'
        ordering = ['title']

    def __str__(self):
        return self.title
