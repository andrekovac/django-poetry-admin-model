# django has its own model class we can use, models.Model -> inherit properties from this class
from django.db import models


class Book(models.Model):  # inside the brackets is where its inheriting from
    """Book is a child class of the Django `Model` class"""

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.title} - {self.author}"
