from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Flower(models.Model):
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  # 
  name = models.CharField(max_length=256)
  # 
  description = models.TextField()
  # using the models tool it knows how to create a date time field. auto_now_add=True use the time right now(when it first gets logged in to database)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# dunder string returns the data as a string
  def __str__(self):
    return self.name

# TESTINGGGGGG