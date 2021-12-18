from django.db import models


class Movie(models.Model):
    title = models.CharField(
        max_length=255,
        default=None,
    )
    year = models.IntegerField(
        default=0,
    )
    rating = models.FloatField(
        default=0,
    )
    summary = models.TextField(
        default=None,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovieGenre(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="genres",
        default=None,
    )
    genre = models.CharField(
        max_length=255,
        default=None,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
