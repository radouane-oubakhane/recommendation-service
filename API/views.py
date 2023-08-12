from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Catalog.serializers import RecommendationSerializer
from Catalog.models import Recommendation

# Create your views here.

# get all recommendations
@api_view(['GET'])
def all_recommendations(request):
    recommendations_list = Recommendation.objects.all()
    if len(recommendations_list) == 0:
        return Response({'message': 'No recommendations generated yet'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RecommendationSerializer(recommendations_list, many=True)
    return Response(serializer.data)



# get recommendations for a specific list of users 
@api_view(['GET'])
def users_recommendations(request, user_ids):
    user_ids = user_ids.split(',')
    recommendations = Recommendation.objects.filter(user_id__in=user_ids)
    if len(recommendations) == 0:
        return Response({'message': 'No recommendations generated for these users'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RecommendationSerializer(recommendations, many=True)
    return Response(serializer.data)



# get recommendations for a specific user
@api_view(['GET'])
def user_recommendations(request, user_id):
    recommendations_list = get_list_or_404(Recommendation, user_id=user_id)
    serializer = RecommendationSerializer(recommendations_list, many=True)
    return Response(serializer.data)
