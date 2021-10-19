from django.urls import path
from . import views
from .serializers import *
urlpatterns = [
    path('todo/',views.TodoList.as_view(),name='todos'),
    path('todo/<int:pk>/',views.TodoDetail.as_view(),name='todo-detail'),

]
