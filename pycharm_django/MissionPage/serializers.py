from rest_framework.serializers import ModelSerializer
from .models import MissionPage


class MissionPageSerializer(ModelSerializer):
    class Meta:
        model = MissionPage
        fields = '__all__'
