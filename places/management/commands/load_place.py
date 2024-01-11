import os.path

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Command to load data from JSON to the DB"

    def add_arguments(self, parser):
        parser.add_argument(
            "urls",
            nargs="+",
            type=str,
            help="Ссылки на GEOJson"
        )

    def _upload_file(self, place, url):
        response = requests.get(url)
        response.raise_for_status()
        return PlaceImage.objects.create(
            place=place,
            image=ContentFile(response.content, os.path.basename(url))
        )

    def handle(self, urls=None, *args, **options):
        for url in urls or []:
            response = requests.get(url)
            response.raise_for_status()
            place_info = response.json()
            place, created = Place.objects.get_or_create(
                title=place_info["title"],
                defaults=dict(
                    short_description=place_info["description_short"],
                    long_description=place_info["description_long"],
                    lat=place_info["coordinates"]["lat"],
                    lon=place_info["coordinates"]["lng"]
                )
            )
            for url in place_info.get("imgs"):
                self._upload_file(place, url)
