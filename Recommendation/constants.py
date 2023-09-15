# Description: Constants for Recommendation app


BOOTSTRAP_SERVERS = ['localhost:9092']


GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_SCHEMA = """
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generate recommendations for all users",
        "description": "Generate recommendations for all users in the database",
        "type": "object",
        "properties": {
        }
    }
    """

GENERATE_RECOMMENDATIONS_FOR_ALL_USERS_TOPIC = 'generate_recommendations_for_all_users'

RECOMMENDATIONS_GENERATED_FOR_ALL_USERS_SCHEMA = """
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Recommendations generated for all users",
        "description": "Recommendations generated for all users in the database",
        "type": "object",
        "properties": {
        }
    }
    """

RECOMMENDATIONS_GENERATED_FOR_ALL_USERS_TOPIC = 'recommendations_generated_for_all_users'