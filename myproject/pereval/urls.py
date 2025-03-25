from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerevalViewSet

router = DefaultRouter()
router.register(r'submitData', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('', include(router.urls)),
]