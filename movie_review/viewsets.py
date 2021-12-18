from rest_framework import viewsets

from movie_review.models import MovieReview
from movie_review.serializers import MovieReviewModelSerializer


class MovieReviewModelViewSet(viewsets.ModelViewSet):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewModelSerializer
