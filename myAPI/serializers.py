from rest_framework import serializers
from myAPI.models import Message


class MessageSerializer(serializers.ModelSerializer):
    # message = serializers.SlugRelatedField(
    #     many=True,
    #     slug_name='name'
    #     queryset = Message.objects.all()
    # )

    class Meta:
        model = Message
        fields = ('id', 'title', 'content')

