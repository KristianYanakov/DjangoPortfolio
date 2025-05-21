from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title