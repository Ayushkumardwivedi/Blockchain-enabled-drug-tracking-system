from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import UINSerializer

class UINViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = UINSerializer