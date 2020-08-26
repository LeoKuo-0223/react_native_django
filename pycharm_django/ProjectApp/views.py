from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectAppSerializer
from .models import ProjectApp


class ProjectAppViewSet(ModelViewSet):
    serializer_class = ProjectAppSerializer
    queryset = ProjectApp.objects.all()
