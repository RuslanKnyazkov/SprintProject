from django.urls import path
from .views import PerevalAddedCreateView, submit_data

urlpatterns = [
    path('submitData/', submit_data, name='submit-data'),
]