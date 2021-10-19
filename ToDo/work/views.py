from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics

class TodoList(APIView):

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
        
    @swagger_auto_schema(request_body=TodoSerializer)
    def post(self, request, format=None):
        request.data['is_completed'] = False
        request.data['user'] = request.user.id
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TodoDetail(APIView):

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TodoSerializer)
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.is_completed = True
        todo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

