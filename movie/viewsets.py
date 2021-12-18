from rest_framework import viewsets, filters

from movie.filters import MovieFilterBackend
from movie.models import Movie
from movie.serializers import MovieModelSerializer


class MovieModelViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    filter_backends = (
        MovieFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    ordering_fields = ("rating",)
    search_fields = ("title",)
