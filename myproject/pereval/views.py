from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Pereval
from .serializers import PerevalSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['post']  # Разрешаем только POST запросы

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