from django.urls import path
from .views import ListMovie

urlpatterns = [
    path('', ListMovie.as_view(), name='home'),
]
