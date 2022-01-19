from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homework(models.Model):
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  url = models.URLField(max_length=200)
  contents = models.TextField()