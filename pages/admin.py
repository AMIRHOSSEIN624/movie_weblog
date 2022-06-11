from django.contrib import admin
from .models import Movie


class AdminMovie(admin.ModelAdmin):
    list_display = ('title', 'genre',)


admin.site.register(Movie, AdminMovie)
