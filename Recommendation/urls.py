from django.urls import path
from . import views



# URL Configuration for API app
urlpatterns = [
    # generate recommendations
    path('', views.generate_recommendations_for_all_users, name='generate-recommendations-for-all-users'),
    path('<int:user_id>/', views.generate_recommendations_for_user, name='generate-recommendations-for-user'),
    path('users/<str:user_ids>/', views.generate_recommendations_for_users, name='generate-recommendations-for-users'),
]

