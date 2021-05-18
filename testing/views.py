from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def greeting_view(request):
    return HttpResponse("Hello this is test case for views.py")

@login_required
def greeting_view_user(request):
    user = request.user
    return HttpResponse('welcome {username}!'.format(username=user))