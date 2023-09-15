from django.db import models

# Create your models here.

class KafkaEvent(models.Model):
    """Event to generate recommendations for all users."""

    date_time = models.DateTimeField()
    topic = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "Date time: " + str(self.date_time) + " , Topic: " + str(self.topic)
    
