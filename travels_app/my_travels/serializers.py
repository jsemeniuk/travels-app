from rest_framework_gis import serializers

from my_travels.models import PlacesVisited


class PlacesSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""

        fields = ("id", "name", "visit_date", "description")
        geo_field = "location"
        model = PlacesVisited