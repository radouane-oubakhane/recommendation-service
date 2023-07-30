from django.urls import path
from . import views



# URL Configuration for API app
urlpatterns = [
    path('', views.get_recommendations, name='get_recommendations'),
    path('<int:user_id>/', views.get_user_recommendations, name='get_user_recommendations'),
]

