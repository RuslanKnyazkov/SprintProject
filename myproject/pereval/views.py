from django.shortcuts import render

from rest_framework import generics
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer

class PerevalAddedCreateView(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


from django.http import JsonResponse
import json


def submit_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = PerevalAddedSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({'status': 'success', 'data': data})  # Пример ответа
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)