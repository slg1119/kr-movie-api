from django.contrib import admin

from movie_review.models import MovieReview


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    fields = [
        "movie",
        "text",
        "rating",
    ]
    list_display = fields + ["created_at", "updated_at"]
