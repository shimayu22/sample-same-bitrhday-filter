from django.urls import path, include
from rest_framework import routers

from sampleapi import views

router = routers.DefaultRouter()
router.register('sampleapi', views.SampleViewSet)

app_name = 'sampleapi'
urlpatterns = [
     path('', include(router.urls))
]