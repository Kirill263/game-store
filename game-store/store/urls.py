from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('genres/', views.all_genres, name='all_genres'),
]
