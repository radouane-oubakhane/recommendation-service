from django.db import models

# Create your models here.

# recommendation model
class Recommendation(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.FloatField()
    timestamp = models.IntegerField()

    def __str__(self) -> str:
        return "User id: " + str(self.user_id) + " , Movie id: " + str(self.movie_id) + " , Rating: " + str(self.rating) + " , Timestamp: " + str(self.timestamp)


