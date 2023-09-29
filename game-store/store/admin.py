from django.contrib import admin
from .models import *


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class DeveloperAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PlatformAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Genre, GenreAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Game, GameAdmin)
