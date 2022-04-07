from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets


class Singerview(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class Songview(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
