from django.urls import path

from .viewsets import *

urlpatterns = [
    path(
        "<int:pk>/",
        MovieReviewModelViewSet.as_view(
            {
                "get": "retrieve",
                "delete": "destroy",
                "patch": "update",
            },
        ),
        name="review_detail_delete_patch",
    ),
    path(
        "",
        MovieReviewModelViewSet.as_view(
            {
                "post": "create",
            },
        ),
        name="review_create",
    ),
]
