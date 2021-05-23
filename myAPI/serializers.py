from rest_framework import serializers
from myAPI.models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'title', 'content', 'counter')
        
        
class MessageSerializerLess(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'title', 'content')




