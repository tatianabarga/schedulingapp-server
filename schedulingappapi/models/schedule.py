from django.db import models
from .user import User

class Schedule(models.Model):
  
  label = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  dates = models.CharField(max_length=100)
  goals = models.CharField(max_length=10000)