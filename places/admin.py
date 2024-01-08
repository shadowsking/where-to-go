from django.contrib import admin
from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        PlaceImageInline
    ]


@admin.register(PlaceImage)
class PlaceImage(admin.ModelAdmin):
    pass
