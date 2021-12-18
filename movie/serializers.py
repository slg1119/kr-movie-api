from rest_framework import serializers

from movie.models import Movie, MovieGenre, Genre


class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class MovieGenreModelSerializer(serializers.ModelSerializer):
    genre = GenreModelSerializer()

    class Meta:
        model = MovieGenre
        fields = ("genre",)


class MovieModelSerializer(serializers.ModelSerializer):
    genres = MovieGenreModelSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        genres = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)

        for genre in genres:
            name = genre.get("genre").get("name")
            if Genre.objects.filter(name=name).exists():
                genre = Genre.objects.get(name=name)
            else:
                genre = Genre.objects.create(name=name)
            MovieGenre.objects.create(
                movie=movie,
                genre=genre,
            )
        return movie


class MovieFilterSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=False)
    genre = serializers.CharField(required=False)
