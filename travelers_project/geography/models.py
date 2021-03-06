import random

from django.db import models
from django.shortcuts import reverse
from slugify import slugify


def image_region(instance, filename):
    return "images/regions/{}/{}".format(slugify(filename), filename)


def image_city(instance, filename):
    return "images/cities/{}/{}".format(slugify(filename), filename)


def image_sight(instance, filename):
    return "images/sights/{}/{}".format(slugify(filename), filename)


class BaseModel(models.Model):

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class RatingMixin(models.Model):
    rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг')

    class Meta:
        abstract = True


class Region(BaseModel):
    title = models.CharField('Название', max_length=255, default='')
    description = models.TextField('Описание', default='', blank=True)
    image = models.FileField(upload_to=image_region, blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ['title']


class CityManager(models.Manager):
    def posted(self):
        return self.filter(posted=True)


class City(BaseModel, RatingMixin):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="city", default=None,
                               null=True, verbose_name="Регион")
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    description = models.TextField(default='', blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, db_index=True, blank=True, verbose_name='Адрес')
    image = models.FileField(upload_to=image_city, blank=True, null=True, verbose_name='Изображение')
    default_zoom = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='Масштаб')
    centre_coordinates = models.CharField(max_length=100, default='', blank=True, verbose_name='Координаты')
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    show_on_mainmap = models.BooleanField(default=True, verbose_name='Показывать на главной карте')
    regional_center = models.BooleanField(default=True, verbose_name='Региональный центр')
    add_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата добавления')
    last_modified_date = models.DateTimeField(null=True, auto_now=True, verbose_name='Дата последнего изменения')
    autotravel_url = models.CharField(max_length=255, default='', blank=True, verbose_name="URL")
    latitude = models.CharField(max_length=100, default='', blank=True, verbose_name='Широта')
    longitude = models.CharField(max_length=100, default='', blank=True, verbose_name='Долгота')

    objects = CityManager()

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']


class TypeOfSights(BaseModel):
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    time = models.CharField(max_length=100, default='', blank=True, verbose_name='Время')
    color = models.CharField(max_length=30, default='#0000FF', verbose_name='Цвет')
    marker = models.CharField(max_length=30, default='marks/flag-export.png', verbose_name='Маркер')

    class Meta:
        verbose_name = 'Тип достопримечательности'
        verbose_name_plural = 'Типы достопримечательностей'
        ordering = ['title']


class Sight(BaseModel, RatingMixin):
    type = models.ManyToManyField(TypeOfSights, related_name='type_sight', verbose_name='Достопримечательности')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='sight', blank=True, null=True,
                             verbose_name='Город')
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    text = models.TextField(default='', verbose_name='Описание')
    image = models.FileField(upload_to=image_sight,
                             max_length=200,
                             blank=True,
                             null=True,
                             verbose_name='Фотография достопримечательности')
    original_coordinates = models.CharField(max_length=100, default='', blank=True, verbose_name='Стянутные координаты')
    coordinates = models.CharField(max_length=100, default='', blank=True, verbose_name='Координаты')
    # широта
    latitude = models.CharField(max_length=100, default='', blank=True, verbose_name='Широта')
    # долгота
    longitude = models.CharField(max_length=100, default='', blank=True, verbose_name='Долгота')
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    regional = models.BooleanField(default=False, verbose_name='В регионе')
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name='Цена')
    add_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата добавления')
    fix_date = models.DateTimeField(null=True, auto_now=True, verbose_name='Дата исправления')
    address = models.CharField(max_length=255, default='', blank=False, verbose_name='Адрес')
    autotravel_url = models.CharField(max_length=255, default='', blank=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечтельности'
        ordering = ['title']


class SectionOfSights(BaseModel):
    types = models.ManyToManyField(TypeOfSights, related_name='type_section_of_sights', blank=True, verbose_name='Типы')
    title = models.CharField(max_length=255, default='', verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел достопримечательностей'
        verbose_name_plural = 'Разделы достопримечательностей'
        ordering = ['title']


class SightPhoto(RatingMixin):
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE,
                              related_name='sight_photo',
                              null=True,
                              verbose_name='Достпримечательность')
    file = models.ImageField(default='', upload_to=image_sight, max_length=200, verbose_name='Изображение')
    posted = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Фотография достопримечательности'
        verbose_name_plural = 'Фотографии достопримечательности'
