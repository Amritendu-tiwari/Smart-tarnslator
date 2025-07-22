from django.urls import path
from .views import suggest_titles

urlpatterns = [
    path('', suggest_titles, name='suggest_titles'),
]