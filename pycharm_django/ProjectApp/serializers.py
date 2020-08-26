from rest_framework.serializers import ModelSerializer
from .models import ProjectApp


class ProjectAppSerializer(ModelSerializer):
    class Meta:
        model = ProjectApp
        fields = '__all__'
