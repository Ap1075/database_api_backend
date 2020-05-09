from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *

class pathAPI(viewsets.ModelViewSet):
    serializer_class = PathSerializer
    queryset = ImagePathDb.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
