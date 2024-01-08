from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage

    readonly_fields = ["get_preview"]

    def get_preview(self, place_image):
        return format_html(
            '<img src="{}" style="max-height:{}px" />',
            place_image.image.url,
            200
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        PlaceImageInline
    ]


@admin.register(PlaceImage)
class PlaceImage(admin.ModelAdmin):
    pass
