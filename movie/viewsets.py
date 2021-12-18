from rest_framework import viewsets

from movie.models import Movie
from movie.serializers import MovieModelSerializer


class MovieModelViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
