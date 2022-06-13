from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Movie(models.Model):
    QUALITY_CHOICES = (
        ('480p', 'blu-ray 480p',),
        ('720p', 'blu-ray 720p',),
        ('1080p', 'blu-ray 1080p',),
    )
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/')
    quality = models.CharField(choices=QUALITY_CHOICES, max_length=5)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    link = models.CharField(max_length=100)
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite', blank=True)

    def get_absolute_url(self):
        return reverse('detail_page', args=[self.id])

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
