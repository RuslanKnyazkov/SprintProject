from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerevalViewSet, PerevalDetailView
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'submitData', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('submitData/<int:pk>/', PerevalDetailView.as_view(), name='pereval-detail'),
    path('', include(router.urls)),

]

