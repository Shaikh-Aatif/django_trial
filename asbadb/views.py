from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from asbadb.models import Credentials

from .serializers import CredentialSerializer

# Create your views here.

def index(request):
    return HttpResponse('Success')

class QuestionsApi(viewsets.ModelViewSet):
    queryset = Credentials.objects.all()

    serializer_class = CredentialSerializer
