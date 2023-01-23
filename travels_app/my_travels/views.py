import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import PlacesVisited, UserConfig
from .forms import EditPlaceForm, NewPlaceForm
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

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

@login_required
def place_detail(request, pk):
    place = get_object_or_404(PlacesVisited, pk=pk)
    return render(request, 'my_travels/place_details.html', {'place': place})

@login_required
def place_edit(request, pk):
    place = get_object_or_404(PlacesVisited, pk=pk)
    if request.method == "POST":
        form = EditPlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect("place_detail", pk=place.pk)
    else:
        form = EditPlaceForm(instance=place)
    return render(request, 'my_travels/place_edit.html', {'form': form})

@login_required
def place_new(request, **kwargs):
    lat = kwargs['location'].split(',')[0]
    lng = kwargs['location'].split(',')[1]
    if request.method == "POST":
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.location = f'POINT({lng} {lat})' 
            place.save()
            return redirect("place_detail", pk=place.pk)
    else:
        form = NewPlaceForm()
    return render(request, 'my_travels/place_edit.html', {'form': form})
class TravelsMapView(TemplateView):

    template_name = "my_travels/map.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)

    def get_context_data(self, request, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["my_travels"] = json.loads(serialize("geojson", PlacesVisited.objects.all()))
        try:
            user_config = UserConfig.objects.get(user = request.user)
            context["map_page_title"] = user_config.map_page_title
        except:
            context["map_page_title"] = "Visited Places"
        return context 
