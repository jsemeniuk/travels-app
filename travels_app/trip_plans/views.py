from django.shortcuts import render, get_object_or_404, redirect
from .models import TripPlan
from .forms import AddNewPlanForm, EditPlanForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import  ListView
from my_travels.models import Places, Tag
from django.db.models import Q

@login_required
def trip_plan_new(request):
    if request.method == "POST":
        form = AddNewPlanForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            return redirect("trip_plan_edit", pk=trip.pk)
    else:
        form = AddNewPlanForm()
    return render(request, 'trip_plans/trip_plan_new.html', {'form': form})


@login_required
def trip_details(request, pk):
    trip = get_object_or_404(TripPlan, pk=pk)
    tags = trip.tag.all()
    places = trip.places.all()
    if len(tags) > 0 and len(places) > 0:
        return render(request, 'trip_plans/trip_details.html', {'trip': trip, 'tags': tags, 'places': places})
    elif len(tags) > 0:
        return render(request, 'trip_plans/trip_details.html', {'trip': trip, 'tags': tags})
    elif len(tags) > 0:
        return render(request, 'trip_plans/trip_details.html', {'trip': trip, 'places': places})
    else:
        return render(request, 'trip_plans/trip_details.html', {'trip': trip})


@login_required
def trip_plan_edit(request, pk):
    trip = get_object_or_404(TripPlan, pk=pk)
    if request.method == "POST":
        form = EditPlanForm(request.POST, instance=trip, user=request.user)
        if form.is_valid():
            trip = form.save()
            trip.user = request.user
            trip.save()
            return redirect("trip_details", pk=trip.pk)
    else:
        form = EditPlanForm(instance=trip, user=request.user)
    return render(request, 'trip_plans/trip_plan_edit.html', {'form': form, 'trip': trip})


@login_required
def trip_check_list_exists(request, pk):
    trip = get_object_or_404(TripPlan, pk=pk)
    if trip.Lists:
        plan_list = trip.lists
        return redirect("list_edit", pk=plan_list)
    else:
        return redirect("lists_all")  

@login_required(login_url='login')
def add_tag_for_trip(request, **kwargs):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect("trip_plan_edit", pk=kwargs['pk'])
    else:
        form = TagForm()
    return render(request, 'my_travels/tag.html', {'form': form})

@login_required(login_url='login')
def delete_trip(request, pk):
    trip = get_object_or_404(TripPlan, pk=pk)
    if request.method == 'GET':
        return render(request, 'trip_plans/confirm_delete.html', {'elem_to_delete': trip, 'pk': pk})
    elif request.method == "POST": 
        trip.delete()
        return redirect("/", pk=pk)

class SearchResultsList(ListView):
    model = TripPlan
    context_object_name = "trips"
    template_name = "trip_plans/trips_all.html"

    def get_queryset(self):
        trips_all = []
        if "tag_id" in self.kwargs:
            trips = TripPlan.objects.filter(user=self.request.user).filter(Q(tag__id=self.kwargs["tag_id"]))
        else:
            query = self.request.GET.get("q")
        
            if query != None:
                search_tags = [tag.pk for tag in Tag.objects.filter(user=self.request.user).filter(Q(tag__icontains=query))]
                trips = TripPlan.objects.filter(user=self.request.user).filter(Q(name__icontains=query) | Q(tag__in=search_tags)).distinct()
            else:
                trips = TripPlan.objects.filter(user=self.request.user)
        for trip in trips:
            trips_all.append({'name':trip.name, 
                               'pk': trip.pk, 
                               'tags': [tag.tag for tag in trip.tag.all()]})
        if len(trips_all) == 0:
            trips_all = False
        return trips_all