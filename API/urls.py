from django.urls import path
from . import views



# URL Configuration for API app
urlpatterns = [
    path('v1/recommendation/', views.get_recommendations, name='get_recommendations'),
    path('v1/recommendation/<int:user_id>/', views.get_user_recommendations, name='get_user_recommendations'),
]

