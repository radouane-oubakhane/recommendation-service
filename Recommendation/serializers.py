from rest_framework import serializers
from .models import KafkaEvent




class KafkaEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafkaEvent
        fields = ['date_time', 'topic']
