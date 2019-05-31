from django.urls import path

from . import views

urlpatterns = [
    path('api/vision', views.vision_api, name='VisionAPI'),
]
