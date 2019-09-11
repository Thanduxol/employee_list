from rest_framework import routers

from employee.api.viewsets import EmployeeAPIView

router = routers.DefaultRouter()
router.register('employee', EmployeeAPIView, base_name='employee')
