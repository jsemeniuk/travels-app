from django.shortcuts import render, get_object_or_404, redirect
from .models import TripPlan
from .forms import AddNewPlanForm, EditPlanForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'trip_plans/trip_details.html', {'trip': trip})

@login_required
def trip_plan_edit(request, pk):
    trip = get_object_or_404(TripPlan, pk=pk)
    if request.method == "POST":
        form = EditPlanForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save()
            trip.user = request.user
            trip.save()
            return redirect("trip_details", pk=trip.pk)
    else:
        form = EditPlanForm(instance=trip)
    return render(request, 'trip_plans/trip_plan_edit.html', {'form': form, 'trip': trip})


@login_required
def trips_all(request):
    trips_all = TripPlan.objects.filter(user=request.user)
    if len(trips_all) == 0:
        trips_all = False
    return render(request, 'trip_plans/trips_all.html', {'trips': trips_all})