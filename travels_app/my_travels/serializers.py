from rest_framework_gis import serializers

from my_travels.models import PlacesVisited


class PlacesSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name", "visit_date", "description", "photo")
        geo_field = "location"
        model = PlacesVisited