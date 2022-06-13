from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie
from .forms import CommentForm
from django.http import HttpResponseRedirect
class ListMovie(generic.ListView):
    model = Movie
    template_name = 'pages/home.html'
    context_object_name = 'movies'


def detail_page(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    #comments
    movie_comments = movie.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = movie
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'pages/detail_page.html', context={
        'movie': movie , 'comment_form': comment_form, 'comments': movie_comments} )
