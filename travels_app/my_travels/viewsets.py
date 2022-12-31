from rest_framework import viewsets
from rest_framework_gis import filters

from my_travels.models import PlacesVisited
from my_travels.serializers import PlacesSerializer


class PlacesViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = PlacesVisited.objects.all()
    serializer_class = PlacesSerializer