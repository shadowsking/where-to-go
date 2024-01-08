from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def show_start_page(request):
    places = Place.objects.all()
    features_collection = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        features_collection["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lon, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("place-details", args=[place.id])
                }
            }
        )
    return render(
        request,
        "index.html",
        context={
            "places": features_collection
        }
    )


def show_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = list(map(lambda i: i.image.url, place.images.all()))
    return JsonResponse(
        {
            "title": place.title,
            "imgs": images,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lat": place.lat,
                "lng": place.lon
            }
        },
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 2
        }
    )
