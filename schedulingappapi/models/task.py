from django.db import models
from .day import Day
from .schedule import Schedule
from .user import User

class Task(models.Model):
  label = models.CharField(max_length=50)
  duration = models.TimeField() # what am i doing here??
  start_time = models.TimeField() # what am i doing here??
  end_time = models.TimeField() # what am i doing here?? do i need this?
  day = models.ForeignKey(Day, on_delete=models.CASCADE)
  schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE) # might change this to many to many later idk. if so REMOVE ON DELETE CASCADE
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  locked_status = models.BooleanField()
  category = models.CharField(max_length=50)