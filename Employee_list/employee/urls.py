from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import EmployeeListView, JSONListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, AjaxDetailView

app_name = 'employee'
urlpatterns = [
    path('employee/ajax', AjaxDetailView.as_view(), name='employee_ajax'),
    path('employee/json', JSONListView.as_view(), name='json'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='delete_employee'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='edit_employee'),
    path('employee/new/', EmployeeCreateView.as_view(), name='new_employee'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('', EmployeeListView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
