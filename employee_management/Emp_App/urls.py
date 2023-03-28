
from django.urls import path
from .views import (
    EmployeeListView, EmployeeCreateView, EmployeeUpdateView,
    EmployeeDeleteView, EmployeeDetailView, EmployeeAPIView,
    EmployeeListAPIView, EmployeeSearchView,
)

app_name = 'Emp_App'

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('emp/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('emp/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('emp/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('api/emp/<int:pk>', EmployeeAPIView.as_view(), name='employee_api'),
    path('api/emp/', EmployeeListAPIView.as_view(), name='employee_api_list'),
    path('emp/search/', EmployeeSearchView.as_view(), name='employee_search'),
    path('emp/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
]
