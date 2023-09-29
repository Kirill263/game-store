from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Genre


def index(request):
    return render(request, 'store/index.html')


def all_genres(request):
    genres = Genre.objects.all()
    return render(request, 'store/genres.html', {'genres': genres})
