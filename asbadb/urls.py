from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework import routers
from asbadb.models import Credentials

from .views import QuestionsApi,index

router = routers.DefaultRouter()
router.register("username", QuestionsApi)



urlpatterns =[
    
    path('' , views.QuestionsApi.as_view({'get': 'retrieve'}), name='homepage',),
    path('', include(router.urls)), 
    path('', index, name="index"),]