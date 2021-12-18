from rest_framework.filters import BaseFilterBackend

from movie.serializers import MovieFilterSerializer


class MovieFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.GET.get("year") and not request.GET.get("genre"):
            return queryset

        serializer = MovieFilterSerializer(
            data=request.GET,
        )

        serializer.is_valid(raise_exception=True)

        year = serializer.validated_data.get("year")
        genre = serializer.validated_data.get("genre")

        if year:
            queryset = queryset.filter(year=year)
        if genre:
            queryset = queryset.filter(genres__genre=genre)

        return queryset
