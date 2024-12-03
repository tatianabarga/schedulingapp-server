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
    start_time = None
    end_time = None
    category = None
    duration = None
    
    if 'day' in request.data and request.data['day']:
      day = Day.objects.get(id=request.data['day'])
      
    if 'start_time' in request.data and request.data['start_time']:
      start_time = request.data['start_time']
      
    if 'end_time' in request.data and request.data['end_time']:
      end_time = request.data['end_time']
      
    if 'category' in request.data and request.data['category']:
      category = request.data['category']
      
    if 'duration' in request.data and request.data['duration']:
      duration = request.data['duration']
    
    task = Task.objects.create(
      start_time=start_time,
      end_time=end_time,
      locked_status = request.data['locked_status'],
      category = category,
      duration = duration,
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