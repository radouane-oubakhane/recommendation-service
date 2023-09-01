from uuid import uuid4
import json
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
# from confluent_kafka.schema_registry import SchemaRegistryClient
# from confluent_kafka.schema_registry.json_schema import JSONSerializer
from .constants import RECOMMENDATIONS_GENERATED_FOR_ALL_USERS_TOPIC
from Catalog.serializers import RecommendationSerializer



class ProducerRecommendationsForAllUsersCreated:
    def __init__(self):
        pass
    # pass recommendations to produce fuction as a parameter
    def produce(self, generated_recommendations):
        # create JSON serializer
        # json_serializer = JSONSerializer(GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_SCHEMA)

        # create a string serializer
        string_serializer = StringSerializer('utf_8')

        # create a producer configuration
        producer_conf = {
            'bootstrap.servers': 'localhost:9092',
            'key.serializer': string_serializer,
        }

        # create a producer
        producer = SerializingProducer(producer_conf)

        # create a schema registry configuration
        # schema_registry_conf = {'url': 'http://localhost:8081'}
        # schema_registry_client = SchemaRegistryClient(schema_registry_conf)

        # create a topic
        topic = RECOMMENDATIONS_GENERATED_FOR_ALL_USERS_TOPIC

        # create a key
        key = str(uuid4())

        # create a value as recommendations list
        serializer = RecommendationSerializer(generated_recommendations, many=True)

        json_data = json.dumps(serializer.data)

        # produce the message
        producer.produce(topic=topic, key=key, value=json_data.encode('utf-8'))

        # flush the producer
        producer.flush()

        # print the message
        print(f"Message produced to the topic {topic}")





























