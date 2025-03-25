from django.shortcuts import render

from rest_framework import generics
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer

class PerevalAddedCreateView(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
