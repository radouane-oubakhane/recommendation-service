from celery import shared_task
import joblib
import numpy as np
import os
import datetime

from Catalog.models import Recommendation


# Determine the absolute path to the joblib file
data_dir = os.path.join(os.path.dirname(__file__), 'data')
params_path = os.path.join(data_dir, 'collab_filter_params.joblib')

# Load the parameters
collaborative_filter_params = joblib.load(params_path)

X = collaborative_filter_params['X']
W = collaborative_filter_params['W']
b = collaborative_filter_params['b']
Y_mean = collaborative_filter_params['Ymean']


# task for running a machine learning model and make recommendations for a all users and save results in database
@shared_task
def run_model():
    p = np.matmul(X, np.transpose(W)) + b
    predictions = p + Y_mean
    # delete all previous recommendations
    Recommendation.objects.all().delete()
    # save the new recommendations
    for i in range(predictions.shape[0]):
        for j in range(predictions.shape[1]):
            recommendation = Recommendation(
                user_id=i + 1, 
                movie_id=j + 1, 
                rating=predictions[i][j],
                timestamp = datetime.datetime.now().timestamp()
                )
            
            recommendation.save()


# task for running a machine learning model and make recommendations for a specific user and save results in database
@shared_task
def run_model_for_user(user_id):
    print("run_model_for_user")

# task for running a machine learning model and make recommendations for a specific users and save results in database
@shared_task
def run_model_for_users(user_ids):
    print("run_model_for_users")




