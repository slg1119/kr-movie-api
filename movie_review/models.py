from django.db import models

from movie.models import Movie


class MovieReview(models.Model):
    movie = models.ForeignKey(
        Movie,
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        default=None,
    )
    rating = models.FloatField(
        default=0,
    )
    vote = models.PositiveIntegerField(
        default=0,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
