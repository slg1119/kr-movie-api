# Generated by Django 4.0 on 2021-12-18 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_moviegenre_genre_alter_moviegenre_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviegenre',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='movie.genre'),
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='movie.movie'),
        ),
    ]
