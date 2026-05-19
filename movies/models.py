from django.db import models

class Movie(models.Model):
    
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    synopsis = models.TextField() 

    def __str__(self):
        return f"{self.title} - {self.publication_year}"
