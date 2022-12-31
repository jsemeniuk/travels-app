import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import PlacesVisited


class TravelsMapView(TemplateView):

    template_name = "map.html"
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["my_travels"] = json.loads(serialize("geojson", PlacesVisited.objects.all()))
        return context 
