from django.db import transaction
from django.test import TestCase
from django.urls import reverse

from movie.models import Movie, MovieGenre


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
            MovieGenre.objects.create(
                movie=movie,
                genre="test",
            )

    def test_given_movie_data_when_list_then_return_200(self):
        """
        정상적으로 리스트가 조회되는지 확인하는 테스트
        """
        response = self.client.get(
            path=reverse("movie_create_list"),
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()[0].get("id"))
        self.assertIsNotNone(response.json()[0].get("title"))
        self.assertIsNotNone(response.json()[0].get("year"))
        self.assertIsNotNone(response.json()[0].get("genres"))
        self.assertIsNotNone(response.json()[0].get("summary"))

    def test_given_movie_data_when_retrieve_then_return_200(self):
        """
        정상적으로 디태알이 조회되는지 확인하는 테스트
        """
        response = self.client.get(
            path=reverse("movie_detail", kwargs={"pk": 1}),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get("id"))
        self.assertIsNotNone(response.json().get("title"))
        self.assertIsNotNone(response.json().get("year"))
        self.assertIsNotNone(response.json().get("genres"))
        self.assertIsNotNone(response.json().get("summary"))
