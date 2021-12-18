from rest_framework import serializers

from movie_review.models import MovieReview


class MovieReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = "__all__"
