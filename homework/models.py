from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homework(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  contents = models.TextField()
  
  def __str__(self):
    return self.title

class Assignment(models.Model):
  id = models.AutoField(primary_key=True)
  hw_id = models.ForeignKey(Homework, on_delete=models.CASCADE, db_column="hw_id")
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  url = models.URLField(max_length=200)
  contents = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)