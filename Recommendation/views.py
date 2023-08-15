from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Recommendation.tasks import run_model, run_model_for_user, run_model_for_users


# Create your views here.


# generate recommendations for all users

@api_view(['GET'])
def generate_recommendations_for_all_users(request):
    # run the model and get the results
    run_model.delay()
    return Response({'message': 'Recommendations engine is running in the background in generation of recommendations for all users and it will take some time'}, status=status.HTTP_200_OK)

# generate recommendations for a specific user

@api_view(['GET'])
def generate_recommendations_for_user(request, user_id):
    run_model_for_user.delay(user_id)
    return Response({'message': 'Recommendations generated successfully'}, status=status.HTTP_200_OK)

# generate recommendations for a specific list of users
@api_view(['GET'])
def generate_recommendations_for_users(request, user_ids):
    run_model_for_users.delay(user_ids)
    return Response({'message': 'Recommendations generated successfully'}, status=status.HTTP_200_OK)

