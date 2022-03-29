from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeeSerializer
from django.db.models import Avg


class EmployeesApi(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_data(self, request):
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'department': request.data.get('department'),
            'salary': request.data.get('salary'),
            'birth_date': request.data.get('birth_date'),
        }
        return data

    def get_object(self, id):
        return Employee.objects.get(id=id)

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            serializer = EmployeeSerializer(self.get_object(pk))
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = self.get_data(request)

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        model = self.get_object(pk)
        data = self.get_data(request)
        serializer = EmployeeSerializer(model, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReportEmployeesApi(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, type=None, *args, **kwargs):
        relatorio = {}
        if type == "age":
            import datetime
            def avg(dates):
                any_reference_date = datetime.date(1900, 1, 1)
                return any_reference_date + sum([date - any_reference_date for date in dates],
                                                datetime.timedelta()) / len(dates)

            days = Employee.objects.all().values_list('birth_date', flat=True)
            avg_days = str(avg(days))

            relatorio = {
                "younger": EmployeeSerializer(Employee.objects.order_by('-birth_date').first()).data,
                "older": EmployeeSerializer(Employee.objects.order_by('birth_date').first()).data,
                "average": avg_days
            }
        elif type == "salary":
            relatorio = {
                "lowest": EmployeeSerializer(Employee.objects.order_by('salary').first()).data,
                "highest": EmployeeSerializer(Employee.objects.order_by('-salary').first()).data,
                "average": Employee.objects.aggregate(Avg('salary'))['salary__avg']
            }

        return Response(relatorio, status=status.HTTP_200_OK)
