from rest_framework import viewsets
from rest_framework_gis import filters

from my_travels.models import Places
from my_travels.serializers import PlacesSerializer


class PlacesVisitedViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    serializer_class = PlacesSerializer

    def get_queryset(self):
        get_user = self.request.user
        queryset = Places.objects.filter(user=get_user, group='AV')
        return queryset
    
class WishlistViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    serializer_class = PlacesSerializer

    def get_queryset(self):
        get_user = self.request.user
        queryset = Places.objects.filter(user=get_user, group='WI')
        return queryset
    