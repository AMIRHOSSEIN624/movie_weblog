from django.shortcuts import render
from django.views import generic
from . models import Movie


class ListMovie(generic.ListView):
    model = Movie
    template_name = 'pages/home.html'
    context_object_name = 'movies'