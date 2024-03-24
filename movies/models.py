from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    film_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=100)
    boolean = models.BooleanField(default=False)
    
    