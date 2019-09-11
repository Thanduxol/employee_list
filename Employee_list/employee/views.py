from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'index.html'
    paginate_by = 10

    def get_ordering(self):
        sort_employee = self.request.GET.get('employee_sort')
        return sort_employee


class JSONResponseMixin:

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context), safe=False,
            **response_kwargs
        )

    def get_data(self, context):
        context = list(context.values())
        return context


class JSONListView(JSONResponseMixin, EmployeeListView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context['object_list'])


class AjaxDetailView(TemplateView):
    template_name = 'employee_ajax.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'new_employee.html'
    fields = ['first_name', 'last_name', 'employment_date', 'job_title', 'description', 'photo']
    success_url = reverse_lazy('employee:index')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'edit_employee.html'
    fields = ['first_name', 'last_name', 'employment_date', 'job_title', 'description', 'photo']
    success_url = reverse_lazy('employee:index')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'delete_employee.html'
    success_url = reverse_lazy('employee:index')
