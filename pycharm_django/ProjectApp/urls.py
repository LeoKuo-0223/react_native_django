from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectAppViewSet

router = DefaultRouter()  # Add
router.register('projectapp', ProjectAppViewSet)  # Add
urlpatterns = [
    path(r'api-token-auth/', views.obtain_auth_token, name='api_login'),
    path('api/', include(router.urls)),
]
