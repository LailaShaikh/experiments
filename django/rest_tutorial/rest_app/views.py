from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_app.serializers import *

from rest_framework import viewsets

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    
