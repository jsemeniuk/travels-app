from rest_framework_gis import serializers

from my_travels.models import Places


class PlacesSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name", "visit_date", "description", "photo", "user", "group")
        geo_field = "location"
        model = Places