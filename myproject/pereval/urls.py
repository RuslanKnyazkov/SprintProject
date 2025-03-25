from django.urls import path
from .views import PerevalAddedCreateView
urlpatterns = [
    path('submitData/', PerevalAddedCreateView.as_view(), name='submit-data'),
]