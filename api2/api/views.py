from django.shortcuts import render

from rest_framework import viewsets
from .models import Task, Role
from .serializers import TaskSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.



class TaskViewAPI(ListAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    # locally apply
    #filter_backends=[DjangoFilterBackend]
    #filterset_fields=['title']

    #search filter
    filter_backends=[SearchFilter]
    search_fields=['title']

