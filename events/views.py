from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Events
from .serializers import EventSerializer
from django.shortcuts import render
import folium


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def map_view(self, request, *args, **kwargs):
        events = self.get_queryset()

        m = folium.Map(location=[47, 8], zoom_start=9)

        for event in events:
            coordinates = (event.lat, event.lon)
            folium.Marker(coordinates, popup=event.title).add_to(m)

        context = {'map': m._repr_html_()}
        return render(request, 'index.html', context)