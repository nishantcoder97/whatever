from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organisation(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    sdescription = models.CharField(max_length=200)
    ldescription = models.CharField(max_length=800)
    place = models.CharField(max_length=20)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    author = User

