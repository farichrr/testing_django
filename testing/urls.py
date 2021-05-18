from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.greeting_view_user, name='greeting_view_user')
]