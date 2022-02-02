from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homework(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  endDate = models.CharField(max_length=200)
  contents = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def summary(self):
    return str(self.contents)[:20]

class Assignment(models.Model):
  id = models.AutoField(primary_key=True)
  hw_id = models.ForeignKey(Homework, on_delete=models.CASCADE, db_column="hw_id")
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  url = models.URLField(max_length=200)
  contents = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  edit_date = models.DateTimeField(auto_now=True)
  
  def date_summary(self):
    return str(self.pub_date)[0:11]