from rest_framework import viewsets
from rest_framework_gis import filters

from my_travels.models import PlacesVisited
from my_travels.serializers import PlacesSerializer


class PlacesViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    serializer_class = PlacesSerializer

    def get_queryset(self):
        get_user = self.request.user
        queryset = PlacesVisited.objects.filter(user=get_user)
        return queryset
    
    