from django.urls import path
from .views import (
    EmployeesApi, ReportEmployeesApi
)

urlpatterns = [
    path('employees/<int:pk>/', EmployeesApi.as_view()),
    path('employees/', EmployeesApi.as_view()),
    path('reports/employees/<type>/', ReportEmployeesApi.as_view())
]
