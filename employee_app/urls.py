from django.urls import path
from .views import EmployeeAPI

urlpatterns = [
    path('', EmployeeAPI.as_view(), name=''),
    path('<str:regid>', EmployeeAPI.as_view(), name='employee-details'),
]