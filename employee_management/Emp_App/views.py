from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EmployeeAPIView(ListView):
    model = Employee
    template_name = 'employee_api.html'
    context_object_name = 'employees'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        employees = self.get_queryset()
        data = {
            'employees': list(employees.values())
        }
        return JsonResponse(data)
