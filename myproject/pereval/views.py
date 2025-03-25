from rest_framework import generics
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class PerevalAddedCreateView(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


