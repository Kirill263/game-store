from django.contrib import admin
from .models import *


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Genre, GenreAdmin)
admin.site.register(Platform)
admin.site.register(Game, GameAdmin)
