from django.db import models
from .user import User

class Schedule(models.Model):
  
  label = models.CharField(max_length=50)
  uid = models.ForeignKey(User, on_delete=models.CASCADE)