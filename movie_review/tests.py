from django.db import transaction
from django.test import TestCase
from django.urls import reverse

from movie.models import Movie, MovieGenre, Genre
from movie_review.models import MovieReview


class MovieTests(TestCase):
    def setUp(self):
        """
        테스트 시작 전에  실행되는 메소드
        """
        with transaction.atomic():
            movie = Movie.objects.create(
                title="test",
                year=1997,
                rating=5.0,
                summary="test",
            )
            genre = Genre.objects.create(
                name="test",
            )
            MovieGenre.objects.create(
                movie=movie,
                genre=genre,
            )
            MovieReview.objects.create(
                movie=movie,
                text="test",
                rating=5.0,
            )

    def test_given_review_movie_data_when_retrieve_then_return_200(self):
        """
        정상적으로 디태알이 조회되는지 확인하는 테스트
        """
        response = self.client.get(
            path=reverse("review_detail_delete_patch", kwargs={"pk": 1}),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get("id"))
        self.assertIsNotNone(response.json().get("text"))
        self.assertIsNotNone(response.json().get("rating"))
        self.assertIsNotNone(response.json().get("created_at"))

    def test_given_review_movie_data_when_create_then_return_201(self):
        """
        정상적으로 데이터가 생성되는지 확인하는 테스트
        """
        response = self.client.post(
            path=reverse("review_create"),
            data={
                "movie": 1,
                "text": "test",
                "rating": 5.0,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json().get("id"))
        self.assertIsNotNone(response.json().get("movie"))
        self.assertIsNotNone(response.json().get("text"))
        self.assertIsNotNone(response.json().get("rating"))

    def test_given_review_movie_data_when_update_then_return_201(self):
        """
        정상적으로 데이터가 수정되는지 확인하는 테스트
        """
        response = self.client.patch(
            path=reverse("review_detail_delete_patch", kwargs={"pk": 1}),
            data={
                "movie": 1,
                "text": "test",
                "rating": 5.0,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get("id"))
        self.assertIsNotNone(response.json().get("movie"))
        self.assertIsNotNone(response.json().get("text"))
        self.assertIsNotNone(response.json().get("rating"))

    def test_given_review_movie_data_when_delete_then_return_201(self):
        """
        정상적으로 데이터가 삭제되는지 확인하는 테스트
        """
        response = self.client.delete(
            path=reverse("review_detail_delete_patch", kwargs={"pk": 1}),
        )

        self.assertEqual(response.status_code, 204)
