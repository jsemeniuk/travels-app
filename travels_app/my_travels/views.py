import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import PlacesVisited
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

def error_page(request, status_code):
    response = render(request, 'error_page.html')
    response.status_code = status_code
    return response

def handler404(request, *args, **argv):
    return error_page(request, 404)

def handler400(request, *args, **argv):
    return error_page(request, 400)

def handler500(request, *args, **argv):
    return error_page(request, 500)

def place_detail(request, pk):
    place = get_object_or_404(PlacesVisited, pk=pk)
    return render(request, 'my_travels/place_details.html', {'place': place})
class TravelsMapView(TemplateView):

    template_name = "my_travels/map.html"
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["my_travels"] = json.loads(serialize("geojson", PlacesVisited.objects.all()))
        return context 
