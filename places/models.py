from django.db import models


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True, null=True)
    description_long = models.TextField('Полное описание', blank=True, null=True)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.title
