from django.urls import path
from . import views



# URL Configuration for API app
urlpatterns = [
    path('recommendations/', views.all_recommendations, name='all-recommendations'),
    path('recommendations/users/<str:user_ids>/', views.users_recommendations, name='users-recommendations'),
    path('recommendations/<int:user_id>/', views.user_recommendations, name='user-recommendations'),
]

