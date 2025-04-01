from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Pereval
from .serializers import PerevalSerializer
from rest_framework.parsers import MultiPartParser, JSONParser


class PerevalViewSet(viewsets.ModelViewSet):
    serializer_class = PerevalSerializer
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

    def get_queryset(self):
        email = self.request.query_params.get('user__email')
        if email:
            return Pereval.objects.filter(user__email = email)

        return Pereval.objects.all()




