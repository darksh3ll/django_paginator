from django.db import models


# Create your models here.
class Movies(models.Model):
    genres = (
        ("Action", "Action"),
        ("Aventure", "Aventure"),
        ("Comedie", "Comedie"),
        ("Drame", "Drame"),
        ("Fantastique", "Fantastique"),
        ("Horreur", "Horreur"),
        ("Policier", "Policier"),
        ("Science-fiction", "Science-fiction"),
        ("Thriller", "Thriller"),
        ("Adulte", "Adulte"),
    )

    title = models.CharField(max_length=40, unique=True)
    poster = models.URLField()
    url = models.URLField()
    content = models.TextField(max_length=255)
    genre = models.CharField(choices=genres, max_length=255)
    active = models.BooleanField(default=True)
    top_film = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Background(models.Model):
    background_img = models.URLField()

    def __str__(self):
        return self.background_img
