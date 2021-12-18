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

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        default=None,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MovieGenre(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        default=None,
        related_name="genres",
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        default=None,
        related_name="genres",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
