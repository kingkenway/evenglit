from rest_framework import serializers
from ..models import Event
from ..models import EventType

class  EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        # fields = ['id', 'title', 'event_type', 'start_time', 'location']

    
    # def validate_title(self, value):
    #     if value  == "a":
    #         raise serializers.ValidationError("End date must be after start date.")   
    #     return value

 
 

class  EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'
        # fields = ['id', 'title', 'event_type', 'start_time', 'location']



# serial = EventSerializer()
# print(repr(serial))