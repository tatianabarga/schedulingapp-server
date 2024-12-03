from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from schedulingappapi.models import Day, Schedule, Task, User
from datetime import date

class TaskView(ViewSet):
  def retrieve(self, request, pk):
    try:
      task = Task.objects.get(pk=pk)
      seriealizer = TaskSerializer(task)
      return Response(seriealizer.data)
    except Task.DoesNotExist as ex:
      return Response({'message': 'task not found'}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    tasks = Task.objects.all()
    schedule = request.query_params.get('schedule', None)
    day = request.query_params.get('day', None)
    
    if schedule is not None:
      tasks = tasks.filter(schedule_id=schedule)
      
    if day is not None:
      tasks = tasks.filter(day_id=day)
      
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    schedule = Schedule.objects.get(id=request.data['schedule'])
    user = User.objects.get(id=request.data['user'])
    day = None
    if 'day' in request.data and request.data['day']:
      day = Day.objects.get(id=request.data['day'])
    
    task = Task.objects.create(
      start_time=request.data['start_time'],
      end_time=request.data['end_time'],
      locked_status = request.data['locked_status'],
      category = request.data['category'],
      duration = request.data['duration'],
      day = day,
      user = user,
      schedule = schedule,
      label = request.data['label'],
    )
    serializer = TaskSerializer(task)
    return Response(serializer.data)
    
  # make update function 
  
  # make delete function
    
    
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'