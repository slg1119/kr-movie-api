from django.urls import path

from .viewsets import *

urlpatterns = [
    path(
        "<int:pk>/",
        MovieModelViewSet.as_view(
            {
                "get": "retrieve",
            },
        ),
        name="movie_detail",
    ),
    path(
        "",
        MovieModelViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            },
        ),
        name="movie_create_list",
    ),
]
