from django.urls import path

from .viewsets import *
from .views import *

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
    path(
        route="vote/<int:pk>/",
        view=VoteGenericAPIVIew.as_view(),
        name="review_vote",
    ),
]
