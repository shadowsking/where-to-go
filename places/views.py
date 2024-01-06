from django.shortcuts import render
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
                    "detailsUrl": ""
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
