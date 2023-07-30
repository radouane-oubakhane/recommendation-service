from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_recommendations(request):
    return HttpResponse("Hello, world. You're at get_recommendations view.")


def get_user_recommendations(request, user_id):
    return HttpResponse("Hello, world. You're at get_user_recommendations view. User ID: %s" % user_id)