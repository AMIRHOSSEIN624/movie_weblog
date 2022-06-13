from django.urls import path
from .views import ListMovie,detail_page

urlpatterns = [
    path('', ListMovie.as_view(), name='home'),
    path('<int:pk>/detail/', detail_page, name= 'detail_page'),
]
