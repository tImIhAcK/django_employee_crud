from django.urls import path
from . import views


app_name = 'employee'
urlpatterns = [
    # path('', views.read_employee, name='employee-list'),
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('create-employee/', views.create_employee, name='create-employee'),
    path('edit-employee/<pk>', views.edit_employee, name='edit-employee'),
    path('delete-employee/<pk>', views.delete_employee, name='delete-employee'),
]