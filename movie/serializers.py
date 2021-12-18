from rest_framework import serializers

from movie.models import Movie, MovieGenre


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ("genre",)


class MovieModelSerializer(serializers.ModelSerializer):
    genres = MovieGenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        genres = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        for genre in genres:
            MovieGenre.objects.create(movie=movie, **genre)
        return movie
