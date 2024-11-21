from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from schedulingappapi.models import Day, Schedule, User

class DayView(ViewSet):
  def retrieve(self, request, pk):
    try:
      day = Day.objects.get(pk=pk)
      serializer = DaySerializer(day)
      return Response(serializer.data)
    except Day.DoesNotExist as ex:
      return Response({'message': 'day not found'}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    days = Day.objects.all()
    schedule = request.query_params.get('schedule', None)
    
    if schedule is not None:
      days = days.filter(schedule_id=schedule)
      
    serializer = DaySerializer(days, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    schedule = Schedule.objects.get(id=request.data['schedule'])
    user = User.objects.get(id=request.data['user'])
    
    day = Day.objects.create(
      schedule=schedule,
      weekday=request.data['weekday'],
      date=request.data['date'],
      user=user,
    )
    
    serializer = DaySerializer(day)
    return Response(serializer.data)
  
  # make update
  
  # make destroy
    
class DaySerializer(serializers.ModelSerializer):
  class Meta:
    model = Day
    fields = ('__all__')