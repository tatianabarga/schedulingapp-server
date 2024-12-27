from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import serializers, status
from schedulingappapi.models import Schedule, User, Day
from django.core.exceptions import ObjectDoesNotExist

class ScheduleView(ViewSet):
  def retrieve(self, request, pk):
    try:
      schedule = Schedule.objects.get(pk=pk)
      serializer = ScheduleSerializer(schedule)
      return Response(serializer.data)
    except Schedule.DoesNotExist as ex:
      return Response({'message': 'schedule not found'}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """returns all lists with option to filter by user(uid) using query"""
    schedules = Schedule.objects.all()
    
    user = request.query_params.get('user', None)
    if user is not None:
      schedules = schedules.filter(user_id=user)
      
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)
     
  def create(self, request):
    user = User.objects.get(id=request.data['user'])
    
    schedule = Schedule.objects.create(
      label=request.data['label'],
      dates=request.data['dates'],
      user=user,
    )
    
    sunday = Day.objects.create(
      schedule=schedule,
      weekday='Sunday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    monday = Day.objects.create(
      schedule=schedule,
      weekday='Monday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    tuesday = Day.objects.create(
      schedule=schedule,
      weekday='Tuesday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    wednesday = Day.objects.create(
      schedule=schedule,
      weekday='Wednesday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    thursday = Day.objects.create(
      schedule=schedule,
      weekday='Thursday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    friday = Day.objects.create(
      schedule=schedule,
      weekday='Friday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    saturday = Day.objects.create(
      schedule=schedule,
      weekday='Saturday',
      date='2000-11-14', # TODO: fix this once date selection for schedules is configured
      user=user,
    )
    
    serializer = ScheduleSerializer(schedule)
    return Response(serializer.data)

  @action(detail=True, methods=['patch'], url_path='add_goal/(?P<schedule_id>[^/.]+)')
  def add_goal(self, request, pk, schedule_id):
    try:
      new_goal = request.data.get('goal',  '').strip()
      if not new_goal:
        return Response({"error": "Goal is required"}, status=status.HTTP_400_BAD_REQUEST)

      schedule = Schedule.objects.get(user_id=pk, schedule_id=schedule_id)
      
      if schedule.goals == '': # == ?
        schedule.goals = new_goal
      else:
        schedule.goals += f" -- {new_goal}"
        
      schedule.save
        
      return Response(None, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
      return Response({"error": "Schedule not found"}, status=status.HTTP_404_NOT_FOUND)
  
  def destroy(self, request, pk):
    try:
      schedule = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
      return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    
    schedule.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedule
    fields = '__all__'