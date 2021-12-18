from django.contrib import admin

from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "year",
        "rating",
        "summary",
    ]
    list_display = fields + ["created_at", "updated_at"]
