from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('genres/', views.all_genres, name='all_genres'),
    path('genre/<slug:genre_slug>/', views.games_by_genre, name='games_by_genre'),
]
