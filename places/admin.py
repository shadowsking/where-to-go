from django.contrib import admin
from .models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(PlaceImage)
class PlaceImage(admin.ModelAdmin):
    pass
