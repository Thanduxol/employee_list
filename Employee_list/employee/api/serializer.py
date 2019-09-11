from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'job_title', 'employment_date', 'description', 'photo')
