from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Genre, Game


def index(request):
    return render(request, 'store/index.html')


def all_genres(request):
    genres = Genre.objects.all()
    return render(request, 'store/genres.html', {'genres': genres})


def games_by_genre(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    games = Game.objects.filter(genres__slug=genre_slug)
    return render(request, 'store/games_by_genre.html', {'genre': genre, 'games': games})
