from confluent_kafka import DeserializingConsumer
# from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from .constants import GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_SCHEMA, GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_TOPIC
from .tasks import generate_recommendations_for_all_users





class ConsumerGenerateRecommendationsForAllUsers:
    def __init__(self):
        pass

    def consume(self):
        # create a string deserializer
        string_deserializer = StringDeserializer('utf_8')
        # create a consumer configuration
        consumer_conf = {
            'bootstrap.servers': 'localhost:9092', 
            'key.deserializer': string_deserializer,
            'value.deserializer': string_deserializer,
            'group.id': 'user_group', 
            'auto.offset.reset': 'earliest'
            }



        # create a consumer
        consumer = DeserializingConsumer(consumer_conf)
        # subscribe to the topic 'generate_recommendations_for_all_users'
        consumer.subscribe([GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_TOPIC])
        # poll the topic
        try: 
            while True:
                # poll the topic
                message = consumer.poll(5.0) 
                # check if the message is not None
                if message is None:
                    continue
                # check if the message has an error
                if message.error():
                    print("Consumer error: {}".format(message.error()))
                    continue
                # print the message
                print("Received message: {}".format(message.value()))
                # call the celery task to generate recommendations for all users
                print("Calling the celery task to generate recommendations for all users")
                generate_recommendations_for_all_users.delay()
        except Exception as e:
            print(f'Exception in Consumer {e}')

        finally:
            # close the consumer
            consumer.close()















# create a function to receive a message
# def receive_message():
#     # create a json deserializer
#     # json_deserializer = JSONDeserializer(GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_SCHEMA)
#     # create a string deserializer
#     string_deserializer = StringDeserializer('utf_8')
#     # create a consumer configuration
#     consumer_conf = {
#         'bootstrap.servers': 'localhost:9092', 
#         'key.deserializer': string_deserializer,
#         'value.deserializer': string_deserializer,
#         'group.id': 'user_group', 
#         'auto.offset.reset': 'earliest'
#         }

#     # create a consumer
#     consumer = DeserializingConsumer(consumer_conf)
#     # subscribe to the topic 'generate_recommendations_for_all_users'
#     consumer.subscribe([GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_TOPIC])
#     # poll the topic
#     while True:
#         try:
#             # poll the topic
#             message = consumer.poll(5.0) 
#             # check if the message is not None
#             if message is None:
#                 continue
#             # check if the message has an error
#             if message.error():
#                 print("Consumer error: {}".format(message.error()))
#                 continue
#             # print the message
#             print("Received message: {}".format(message.value()))
#             # call the celery task to generate recommendations for all users
#             print("Calling the celery task to generate recommendations for all users")
#             generate_recommendations_for_all_users.delay()
#         except Exception as e:
#             print(f'Exception in receive_message {e}')
#             break