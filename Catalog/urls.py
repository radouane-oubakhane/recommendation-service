from django.urls import path
from . import views



# URL Configuration for API app
urlpatterns = [
    # get recommendations
    path('', views.all_recommendations, name='all-recommendations'),
    path('<int:user_id>/', views.user_recommendations, name='user-recommendations'),
    path('users/<str:user_ids>/', views.users_recommendations, name='users-recommendations'),
]

