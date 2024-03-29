from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200, unique=True)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    position = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядковый номер изображения',
        db_index=True
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.position} {self.place.title}"
