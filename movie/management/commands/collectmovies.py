import json
import sys
import requests

from django.core.management.base import BaseCommand
from django.db import OperationalError, transaction

from movie.models import Movie, MovieGenre


class Command(BaseCommand):
    URL = "https://yts.mx/api/v2/list_movies.json"

    help = "Get the movies from 'https://yts.mx/api/v2/list_movies.json'"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            self.style.WARNING("Collecting movies...")
            data = self._get_movie_data()
            movies = data["data"]["movies"]
            for movie in movies:
                with transaction.atomic():
                    movie_data = Movie.objects.create(
                        title=movie.get("title"),
                        year=movie.get("year"),
                        rating=movie.get("rating"),
                        summary=movie.get("summary"),
                    )
                    for genre in movie.get("genres"):
                        MovieGenre.objects.create(
                            movie=movie_data,
                            genre=genre,
                        )

        except OperationalError:
            self.stdout.write(
                self.style.ERROR(
                    "Did you run the 'python manage.py migrate' command?",
                )
            )
            sys.exit()
        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created the movie data.",
            )
        )

    def _get_movie_data(self):
        request = requests.get(self.URL)
        return request.json()
