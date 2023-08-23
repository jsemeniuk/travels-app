import json
from random import choice
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.views.generic.list import  ListView

from .models import Places, Tag
from lists.models import Lists
from .forms import EditPlaceForm, NewPlaceForm, TagForm
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


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


@login_required(login_url='login')
def place_detail(request, pk):
    places_all = Places.objects.filter(user=request.user)
    place = get_object_or_404(Places, pk=pk)
    tags = place.tag.all()
    suggestions = [choice(places_all) for i in range(3)]
    if len(tags) > 0:
        return render(request, 'my_travels/place_details.html', {'place': place, 'tags': tags, "suggestions" : suggestions})
    else:
        return render(request, 'my_travels/place_details.html', {'place': place, "suggestions" : suggestions})

@login_required(login_url='login')
def place_edit(request, pk):
    place = get_object_or_404(Places, pk=pk)
    if place.group == 'AV':
        group_elem = True
    else:
        group_elem = False
    if request.method == "POST":
        form = EditPlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save()
            place.user = request.user
            if request.POST.get('group_check') == 'on':
                place.group = 'AV'
            else:
                place.group = 'WI'
            
            place.save()
            return redirect("place_detail", pk=place.pk)
    else:
        form = EditPlaceForm(instance=place)
    return render(request, 'my_travels/place_edit.html', {'form': form, 'place': place, 'group_elem': group_elem})

@login_required(login_url='login')
def place_new(request, **kwargs):
    lat = kwargs['location'].split(',')[0]
    lng = kwargs['location'].split(',')[1]
    if request.method == "POST":
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.location = f'POINT({lng} {lat})' 
            if request.POST.get('group_check') == 'on':
                place.group = 'AV'
            else:
                place.group = 'WI'
            place.save()
            return redirect("place_detail", pk=place.pk)
    else:
        form = NewPlaceForm()
    return render(request, 'my_travels/place_add.html', {'form': form})
    
@login_required(login_url='login')
def place_check_list_exists(request, pk):
    place = get_object_or_404(Places, pk=pk)
    try:
        list_for_place = Lists.objects.get(place_id=place).pk
        return redirect("list_edit", pk=list_for_place)
    except ObjectDoesNotExist:
        return redirect("list_place_new", place_id=pk)      

@login_required(login_url='login')
def add_tag(request, **kwargs):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect("place_edit", pk=kwargs['pk'])
    else:
        form = TagForm()
    return render(request, 'my_travels/tag.html', {'form': form})

@login_required(login_url='login')
def delete_place(request, pk):
    place = get_object_or_404(Places, pk=pk)
    if request.method == 'GET':
        return render(request, 'my_travels/confirm_delete.html', {'elem_to_delete': place, 'pk': pk})
    elif request.method == "POST": 
        place.delete()
        return redirect("/", pk=pk)

class TravelsMapView(TemplateView):

    template_name = "my_travels/map.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)

    def get_context_data(self, request, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["visited_places"] = json.loads(serialize("geojson", Places.objects.all()))
        context["wishlist"] = json.loads(serialize("geojson", Places.objects.all()))
        return context 


class SearchResultsList(ListView):
    model = Places
    context_object_name = "places"
    template_name = "my_travels/places_all.html"

    def get_queryset(self):
        places_all = []
        if "tag_id" in self.kwargs:
            places = Places.objects.filter(user=self.request.user).filter(Q(tag__id=self.kwargs["tag_id"]))
        else:
            query = self.request.GET.get("q")
        
            if query != None:
                search_tags = [tag.pk for tag in Tag.objects.filter(user=self.request.user).filter(Q(tag__icontains=query))]
                places = Places.objects.filter(user=self.request.user).filter(Q(name__icontains=query) | Q(tag__in=search_tags)).distinct()
            else:
                places = Places.objects.filter(user=self.request.user)
        for place in places:
            if place.group == 'AV':
                status = 'Visited'
            elif place.group == 'WI':
                status = 'Wishlist'
            places_all.append({'name':place.name, 
                               'group': status, 
                               'pk': place.pk, 
                               'tags': [tag.tag for tag in place.tag.all()]})
        if len(places_all) == 0:
            places_all = False
        return places_all