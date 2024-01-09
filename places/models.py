from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200, unique=True)
    description_short = models.TextField('Короткое описание', blank=True, null=True)
    description_long = HTMLField('Полное описание', blank=True, null=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    position = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядковый номер изображения'
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.position} {self.place.title}"
