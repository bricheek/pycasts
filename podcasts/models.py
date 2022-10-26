from django.db import models
from unittest.util import _MAX_LENGTH


class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        #return super().__str__()
        return f"{self.podcast_name}: {self.title}"

    