from django.db import models


class Region(models.Model):
    title = models.CharField('Название', max_length=255, default='', blank=False)
    description = models.TextField('Описание', default='', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class CityManager(models.Manager):
    def posted(self):
        return self.filter(posted=True)


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="city",default=None, blank=True, null=True, verbose_name="Регион")
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    description = models.TextField(default='', blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Адрес')
    default_zoom = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='Масштаб')
    centre_coordinates = models.CharField(max_length=100, default='', blank=True, verbose_name='Координаты')
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    show_on_mainmap = models.BooleanField(verbose_name='Показывать на гавной карте')
    regional_center = models.BooleanField(default=True, verbose_name='Региональный центр')
    add_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата добавления')
    last_modified_date = models.DateTimeField(null=True, auto_now=True, verbose_name='Дата последнего изменения')
    autotravel_url = models.CharField(max_length=255, default='', blank=True, verbose_name="URL")

    objects = CityManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class TypeOfSights(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    time = models.CharField(max_length=100, default='', blank=True, verbose_name='Время')
    color = models.CharField(max_length=30, default='#0000FF', verbose_name='Цвет')
    marker = models.CharField(max_length=30, default='marks/flag-export.png', verbose_name='Маркер')

    class Meta:
        verbose_name = 'Тип достопримечательности'
        verbose_name_plural = 'Типы достопримечательностей'

    def __str__(self):
        return self.title


class Sight(models.Model):
    type = models.ManyToManyField(TypeOfSights, related_name='type_sight', verbose_name='Достопримечательности')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Город')
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    text = models.TextField(default='', verbose_name='Описание')
    original_coordinates = models.CharField(max_length=100, default='', blank=True, verbose_name='Стянутные координаты')
    coordinates = models.CharField(max_length=100, default='', blank=True, verbose_name='Координаты')
    posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    regional = models.BooleanField(default=False, verbose_name='В регионе')
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name='Цена')
    add_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата добавления')
    fix_date = models.DateTimeField(null=True, auto_now=True, verbose_name='Дата исправления')
    address = models.CharField(max_length=255, default='', blank=True, verbose_name='Адрес')
    autotravel_url = models.CharField(max_length=255, default='', blank=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечтельности'

    def __str__(self):
        return self.title


class SectionOfSights(models.Model):
    types = models.ManyToManyField(TypeOfSights, blank=True, verbose_name='Типы')
    title = models.CharField(max_length=255, default='', verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел достопримечательностей'
        verbose_name_plural = 'Разделы достопримечательностей'

    def __str__(self):
        return self.title


class SightPhoto(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, related_name='sigth_photo', null=True, verbose_name='Достпримечательность')
    file = models.ImageField(default='', upload_to='images/photo/', verbose_name='Изображение')
    posted = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Фотография достопримечательности'
        verbose_name_plural = 'Фотографии достопримечательности'