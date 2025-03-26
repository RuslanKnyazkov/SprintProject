from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Pereval
from .serializers import PerevalSerializer
from rest_framework.parsers import MultiPartParser, JSONParser

class PerevalDetailView(APIView):
    http_method_names = ['get']

    def get_object(self, pk):
        try:
            return Pereval.objects.get(pk = pk)
        except Exception as e:
            return Response(status= status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        try:
            pereval = self.get_object(pk)
            serializer = PerevalSerializer(pereval)
            print(pereval, serializer)
            return Response(serializer.data)
        except Pereval.DoesNotExist:
            return Response(
                {"error": "Перевал с указанным ID не найден"},
                status=status.HTTP_404_NOT_FOUND
            )



class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['post']
    parser_classes = [MultiPartParser, JSONParser]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Отправлено успешно',
                'id': serializer.instance.id
            }, status=status.HTTP_200_OK, headers=headers)

        except Exception as e:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'Ошибка сервера: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
