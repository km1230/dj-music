from django.db import models

from .choices import Genre


# Create your models here.
class Album(models.Model):
    """Album model."""
    title = models.TextField()
    year = models.TextField()
    genre = models.CharField(max_length=20, choices=Genre.choices(), default=Genre.pop.value)

    def __str__(self):
        return self.title

    class JSONAPIMeta:
        """JSON API meta information."""
        resource_name = "albums"

class Song(models.Model):
    """Song model."""
    title = models.TextField()
    singer = models.TextField()
    composer = models.TextField()
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title

    class JSONAPIMeta:
        """JSON API meta information."""
        resource_name = "songs"
