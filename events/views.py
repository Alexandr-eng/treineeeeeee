from rest_framework import viewsets
from .models import Events
from .serializers import EventSerializer
from django.shortcuts import render
import folium

def index(request):
    events = Events.objects.all()

    m = folium.Map(location=[56.149416, 40.400494], zoom_start=9)

    for event in events:
        coordinates = (event.lat, event.lon)
        folium.Marker(coordinates).add_to(m)

    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer