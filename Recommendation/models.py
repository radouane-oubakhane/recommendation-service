from django.db import models

# Create your models here.


# User model for recommendation app 
class User(models.Model):

    GENDER_CHOICES = [
        'M', 'Male',
        'F', 'Female',
        'O', 'Other'
    ] 
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    preferences = models.TextField()
    favorite_movies = models.TextField()
    favorite_directors = models.TextField()
    favorite_actors = models.TextField()
    saved_movies = models.TextField()
    watched_movies = models.TextField()
    watch_list = models.TextField()
    

    def __str__(self):
        return self.username