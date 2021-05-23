from django.shortcuts import render
from myAPI.serializers import MessageSerializer
from rest_framework import generics
from myAPI.models import Message
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class MessageView(generics.ListCreateAPIView):
    '''This view is allowing an authorized user to create a message '''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



class MessageChange(generics.RetrieveUpdateDestroyAPIView):
    '''This view allows an authorized user to edit or delete a given message'''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)



class MessageReadOnly(generics.RetrieveAPIView):

    '''This view is allowing an authorized user to see a message. While this happens counter will
    be increased by 1'''

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, pk):
        m = Message.objects.get(id=pk)
        m.counter += 1
        m.save()
        serializer = MessageSerializer(m)
        return Response(serializer.data)









