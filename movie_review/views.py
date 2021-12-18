from rest_framework import generics
from rest_framework.response import Response

from movie_review.models import MovieReview


class VoteGenericAPIVIew(generics.GenericAPIView):
    queryset = MovieReview.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.vote += 1
        instance.save()
        return Response(
            {
                "success": "You have successfully voted",
            }
        )

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.vote == 0:
            return Response(
                {
                    "success": "You have successfully unvoted",
                }
            )
        instance.vote -= 1
        instance.save()
        return Response(
            {
                "success": "You have successfully unvoted",
            }
        )
