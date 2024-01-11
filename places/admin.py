from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage

MAX_HEIGHT = 200
MAX_WIDTH = 687


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage

    readonly_fields = ['get_preview']
    ordering = ['position']

    def get_preview(self, place_image):
        return format_html(
            '<img src="{}" style="max-height:{}px;max-width:{}px" />',
            place_image.image.url,
            MAX_HEIGHT,
            MAX_WIDTH
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        PlaceImageInline
    ]


@admin.register(PlaceImage)
class PlaceImage(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['position']
    raw_id_fields = ('place',)
