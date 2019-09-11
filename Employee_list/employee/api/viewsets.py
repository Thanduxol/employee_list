from rest_framework import viewsets, authentication

from employee.models import Employee
from .serializer import EmployeeSerializer


class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [authentication.SessionAuthentication]
    lookup_field = 'id'
