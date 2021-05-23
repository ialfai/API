from rest_framework import serializers
from myAPI.models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'title', 'content')




