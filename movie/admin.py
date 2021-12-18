from django.contrib import admin

from movie.models import Movie, MovieGenre, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "year",
        "rating",
        "summary",
    ]
    list_display = fields + ["created_at", "updated_at"]


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    fields = [
        "movie",
        "genre",
    ]
    list_display = fields + ["created_at", "updated_at"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = [
        "name",
    ]
    list_display = fields + ["created_at", "updated_at"]
