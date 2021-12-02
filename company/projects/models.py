from django.db import models

# Create your models here.


class Post(models.Model):
    title =  models.CharField(max_length=100)
    content =  models.TextField(blank=True)
    photo = models.URLField(blank=True)
    price =  models.CharField(max_length=100)
    host_end = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title