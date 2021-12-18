from django.db import transaction
from django.test import TestCase
from django.urls import reverse

from movie.models import Movie, MovieGenre, Genre


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

    def test_given_movie_data_when_list_then_return_200(self):
        """
        정상적으로 리스트가 조회되는지 확인하는 테스트
        """
        response = self.client.get(
            path=reverse("movie_create_list"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get("results")[0].get("id"))
        self.assertIsNotNone(response.json().get("results")[0].get("title"))
        self.assertIsNotNone(response.json().get("results")[0].get("year"))
        self.assertIsNotNone(response.json().get("results")[0].get("genres"))
        self.assertIsNotNone(response.json().get("results")[0].get("summary"))

    def test_given_movie_data_when_retrieve_then_return_200(self):
        """
        정상적으로 디태알아 조회되는지 확인하는 테스트
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

    def test_given_movie_data_when_create_then_return_201(self):
        """
        정상적으로 데이터가 생성되는지 확인하는 테스트
        """
        response = self.client.post(
            path=reverse(
                "movie_create_list",
            ),
            data={
                "title": "test",
                "year": 1997,
                "rating": 5.0,
                "summary": "test",
                "genres": [{"genre": {"name": "Comedy"}}, {"genre": {"name": "Drama"}}],
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
