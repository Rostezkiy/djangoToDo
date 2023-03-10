from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('lists', views.ListViewSet)
router.register('tasks', views.TaskViewSet)

app_name = 'todo_drf'
urlpatterns = [
    path('', include(router.urls)),
]
