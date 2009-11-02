from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from models import Event, Speaker

def event(request, slug):
    event = get_object_or_404(Event, slug = slug)
    return render_to_response('event.html', {
        'event': event,
        'speakers': Speaker.objects.filter(
            session__event = event
        ).distinct()
    })
