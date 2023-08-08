from django.db import models

# Create your models here.

# recommendation model
class Recommendation(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.FloatField()
    timestamp = models.IntegerField()

