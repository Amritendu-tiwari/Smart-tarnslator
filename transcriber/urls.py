from django.urls import path
from .views import transcribe

urlpatterns = [
    path('', transcribe, name='transcribe'),
]