from django.shortcuts import render
from rest_framework import viewsets
from .models import song,podcast,audiobook
from .serializers import song_Serializer,podcast_Serializer,audiobook_Serializer
# Create your views here.

class SongViewSet(viewsets.ModelViewSet):

    queryset = song.objects.all()
    serializer_class = song_Serializer


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = podcast.objects.all()
    serializer_class = podcast_Serializer


class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = audiobook.objects.all()
    serializer_class = audiobook_Serializer