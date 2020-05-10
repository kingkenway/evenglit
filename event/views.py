from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Event
from django.contrib.auth.models import User
from .forms import EventForm
from django.contrib import messages
import datetime
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def event_home(request):
    events = Event.active.all()
    date = datetime.datetime.now()
    context = {'events': events, 'date': date}
    return render(request, 'event/home.html', context)

def event_detail(request, pk, slug):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'event/event_detail.html', context)

@login_required
def create_event(request, id=0):
   
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.organiser = request.user
            messages.success(request, 'Event successfully Created!')
            post = form.save()
        else:
            messages.error(request, 'This form is invalid.')
    else:
        form = EventForm()
    
    return render(request, "event/create.html", {'form': form})


@login_required
def edit_event(request, id):
    event = get_object_or_404(Event, pk=id)
    event_url = reverse('edit_event', kwargs={'id': event.id})
    
    if event.organiser != request.user:
        return redirect(create_event)

    if request.method == "GET":
        form = EventForm(instance=event) # Load form parameters with ID provided.

    else:
        form = EventForm(request.POST, request.FILES, instance=event) # Update event with the loaded/modified inputs/

        if form.is_valid():
            post = form.save(commit=False)
            post.organiser = request.user
            messages.success(request, 'Event updated Successfully!')
            form.save()
            return redirect(event_url)

        else:
            messages.error(request, 'This form is invalid.')
        # return redirect('/employee/list')

    return render(request, "event/edit.html", {'form': form, 'event': event})

@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, pk=id)
    if event.organiser == request.user:
        event.delete()
        messages.success(request, 'Event deleted Successfully!')

        return redirect(create_event)
    messages.error(request, 'Unauthorised to Delete!')    
    return redirect(create_event)

    

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    events = Event.objects.filter(organiser_id=user.id)
    context = {'user': user, 'events': events}
    return render(request, "event/user.html", context)



# def handler404(request):
#     return render(request, '404.html', status=404)


# {{ object.pub_date|date:"D d M Y" }} {{ object.pub_date|time:"H:i" }} -->
# https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date