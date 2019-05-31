from django.urls import path

from . import views

urlpatterns = [
    path('', views.vision_api, name='VisionAPI'),
]
