from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import AddNewEventForm, EditEventForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from my_travels.models import Places, Tag
from datetime import datetime, timedelta, date
import calendar
from django.db.models import Q


@login_required
def event_new(request):
    if request.method == "POST":
        form = AddNewEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect("events_calendar")
    else:
        form = AddNewEventForm()
    return render(request, 'events_calendar/event_new.html', {'form': form})

class EventsCalendar:
    def __init__(self, day, month, year, request):
        self.day = day
        self.month = month
        self.year = year
        self.request = request
        self.events = self.filter_events(self.year, self.month, self.day, self.request)
        self.events_long = True if len(self.events) > 2 else False

    def filter_events(self, year, month, day, request):
        events_all = Event.objects.filter(user=request.user)
        events = []
        for event in events_all:
            if event.start_date == event.end_date:
                if event.start_date == date(year, month, day):
                    events.append(event)
            else:
                date_delta = event.end_date - event.start_date
                for i in range(date_delta.days+1):
                    event_date = event.start_date + timedelta(days=i)
                    if event_date == date(year, month, day):
                        events.append(event)
        return events

def events_list(request, **kwargs):
    if 'month' in kwargs and 'year' in kwargs:
        calendar_month = int(kwargs['month'])
        calendar_year = int(kwargs['year'])
    else: 
        calendar_year = datetime.today().year
        calendar_month = datetime.today().month

    if calendar_month == 12:
        next_month = 1
        next_year = calendar_year + 1
    else:
        next_month = calendar_month + 1
        next_year = calendar_year

    if calendar_month == 1:
        prev_month = 12
        prev_year = calendar_year - 1
    else:
        prev_month = calendar_month - 1
        prev_year = calendar_year
    if request.user != AnonymousUser():
        events_all = Event.objects.filter(user=request.user, start_date__month=calendar_month)
    else:
        events_all = Event.objects.filter(user=None, start_date__month=calendar_month)
    return render(request, 'events_calendar/events_list.html', {'month': f'{calendar_month}.{calendar_year}','next_month': next_month, 'next_year': next_year, 'prev_month': prev_month, 'prev_year': prev_year, "events": events_all})

@login_required
def events_calendar(request, **kwargs):
    if 'month' in kwargs and 'year' in kwargs:
        calendar_month = int(kwargs['month'])
        calendar_year = int(kwargs['year'])
    else: 
        calendar_year = datetime.today().year
        calendar_month = datetime.today().month
    
    create_calendar = calendar.month(calendar_year, calendar_month).split('\n')
    month_header = create_calendar[0]
    days_header = create_calendar[1].split(' ')
    cal = calendar.Calendar()
    month_days_all = [day for day in cal.itermonthdays(calendar_year, calendar_month)]
    events_all = Event.objects.filter(user=request.user, start_date__month=calendar_month)   
    days_split = []
    for i in range(0, len(month_days_all), 7):
        days_for_calendar = [EventsCalendar(day, calendar_month, calendar_year, request) if day != 0 else '' for day in month_days_all[i:i+7] ]
        days_split.append(days_for_calendar)

    if calendar_month == 12:
        next_month = 1
        next_year = calendar_year + 1
    else:
        next_month = calendar_month + 1
        next_year = calendar_year

    if calendar_month == 1:
        prev_month = 12
        prev_year = calendar_year - 1
    else:
        prev_month = calendar_month - 1
        prev_year = calendar_year
    return render(request, 'events_calendar/calendar.html', {'month': month_header, 'days': days_header, 'calendar': days_split, 'delta': 0, 'next_month': next_month, 'next_year': next_year, 'prev_month': prev_month, 'prev_year': prev_year})


@login_required
def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    tags = event.tag.all()
    places = event.places.all()
    if len(tags) > 0 and len(places) > 0:
        return render(request, 'events_calendar/event_details.html', {'event': event, 'tags': tags, 'places': places})
    elif len(tags) > 0:
        return render(request, 'events_calendar/event_details.html', {'event': event, 'tags': tags})
    elif len(places) > 0:
        return render(request, 'events_calendar/event_details.html', {'event': event, 'places': places})
    else:
        return render(request, 'events_calendar/event_details.html', {'event': event})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EditEventForm(request.POST, instance=event, user=request.user)
        if form.is_valid():
            event = form.save()
            event.user = request.user
            event.save()
            return redirect("event_details", pk=event.pk)
    else:
        form = EditEventForm(instance=event, user=request.user)
    return render(request, 'events_calendar/event_edit.html', {'form': form, 'event': event})

@login_required(login_url='login')
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'GET':
        return render(request, 'events_calendar/confirm_delete.html', {'elem_to_delete': event, 'pk': pk})
    elif request.method == "POST": 
        event.delete()
        return redirect("/", pk=pk)