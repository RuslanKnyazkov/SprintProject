from django.urls import path, include
from .views import PerevalViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'submitData', PerevalViewSet, basename='pereval')


urlpatterns = [
    path('', include(router.urls)),
]
