from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title



