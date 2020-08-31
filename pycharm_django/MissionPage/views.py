from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MissionPageSerializer
from .models import MissionPage


# Create your views here.

class MissionPageViewSet(ModelViewSet):
    serializer_class = MissionPageSerializer
    queryset = MissionPage.objects.all()
