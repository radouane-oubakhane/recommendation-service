from celery import shared_task


# task for running a machine learning model and make recommendations for a all users and save results in database
@shared_task
def run_model():
    print("run_model for all users")


# task for running a machine learning model and make recommendations for a specific user and save results in database
@shared_task
def run_model_for_user(user_id):
    print("run_model_for_user")

# task for running a machine learning model and make recommendations for a specific users and save results in database
@shared_task
def run_model_for_users(user_ids):
    print("run_model_for_users")