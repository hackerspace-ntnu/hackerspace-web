from django.shortcuts import render
from events.models import Event, Thumbnail
from edit.models import EventEditForm
from django import forms


def index(request):
    event_list = Event.objects.order_by('-date')
    event_thumbnail_list = Thumbnail.objects.all()
    context = {
        'event_list': event_list,
        'event_thumbnail_list': event_thumbnail_list
    }

    return render(request, 'events.html', context)


def event(request, event_id):
    requested_event = Event.objects.get(pk=event_id)
    form = EventEditForm(initial={
        'event_id': event_id,
        'ingress_content': requested_event.ingress_content,
        'main_content': requested_event.main_content
    })
    form.fields['event_id'].widget = forms.HiddenInput()
    context = {
        'event': requested_event,
        'form': form
    }

    return render(request, 'event.html', context)
