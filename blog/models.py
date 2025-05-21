from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # user = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title