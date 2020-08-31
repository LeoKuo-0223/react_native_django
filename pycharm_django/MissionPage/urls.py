from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter  # Add
from .views import MissionPageViewSet  # Modify

router = DefaultRouter()  # Add
router.register('MissionPage', MissionPageViewSet)  # Add
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/mission/', include(router.urls)),
]
