# Generated by Django 4.0 on 2021-12-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviereview',
            name='vote',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
