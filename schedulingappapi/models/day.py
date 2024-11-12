from django.db import models
from .schedule import Schedule
from .user import User

class Day(models.Model):
  schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
  weekday = models.CharField(max_length=50)
  date = models.DateField()
  uid = models.ForeignKey(User, on_delete=models.CASCADE)