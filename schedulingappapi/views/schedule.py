from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from schedulingappapi.models import Schedule, User

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
      schedules = schedules.filter(uid=user)
      
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)
     
  def create(self, request):
    user = User.objects.get(id=request.data['user'])
    
    schedule = Schedule.objects.create(
      label=request.data['label'],
      user=user,
    )
    
    serializer = ScheduleSerializer(schedule)
    return Response(serializer.data)
    
  # make update function
  
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