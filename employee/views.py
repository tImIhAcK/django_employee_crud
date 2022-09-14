from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages


class EmployeeListView(ListView):
    queryset = Employee.objects.all()
    context_object_name = 'employees'
    paginate_by = 10
    template_name = 'employee/list.html'
    
# def read_employee(request):
#     return render(request, 'employee/list.html')

def create_employee(request):
    form = EmployeeForm
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f'{obj.name} created sucessfully')
            obj.save
            return redirect('employee:employee-list')
    return render(request, 'employee/create.html', context={'form': form,})

def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            obj = form.save()
            messages.info(request, f'{obj.name} updated sucessfully')
            obj.save()
            return redirect('employee:employee-list')
            
    context = {
        'employee': employee,
        'form': form
    }
    return render(request, 'employee/edit.html', context)

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method =='POST':
        employee.delete()
        messages.error(request, f'Employee delete....')
        return redirect('employee:employee-list')
        
    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)
