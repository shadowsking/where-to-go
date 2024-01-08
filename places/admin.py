from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html


from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage

    readonly_fields = ['get_preview']
    ordering = ['position']

    def get_preview(self, place_image):
        return format_html(
            '<img src="{}" style="max-height:{}px" />',
            place_image.image.url,
            200
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
