from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE


class Post(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
    author = models.ForeignKey(
        'auth.User',
        on_delete=CASCADE,
    )
    

    body = models.TextField()
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
