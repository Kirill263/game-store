from django.db import models
from tinymce import models as tinymce_models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    description = tinymce_models.HTMLField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    cover_image = models.ImageField(upload_to='game_covers/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
