from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.greeting_view, name='greeting_view')
]