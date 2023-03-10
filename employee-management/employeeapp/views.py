from django.shortcuts import render, redirect
from django.http import HttpResponse
from employeeapp.forms import EmployeeForm
from employeeapp.models import Employee

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST["name"]
        all_employee = Employee.objects.filter(fname__contains = name)
        return render(request, "index.html", {"all_employee": all_employee})
    else: 
        all_employee = Employee.objects.all()
        return render(request, "index.html", {"all_employee": all_employee})

def create(request):
    if request.method == "POST":
        # save the data
        form = EmployeeForm(request.POST, request.FILES)       
        if form.is_valid():
            form.save()
            return redirect('/')

    else:      
        form = EmployeeForm()
        return render(request, "create.html", {"form": form})
def delete(request, emp_id):
    emp = Employee.objects.get(pk = emp_id)
    emp.delete()
    return redirect('/')


def edit(request, emp_id):
    # checking if the edit request is being made
    if request.method == "POST":
        emp = Employee.objects.get(pk = emp_id)
        form = EmployeeForm(instance= emp, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # pulling date of employee that wants to be edited
        emp = Employee.objects.get(pk = emp_id)
        # send data to the edit form
        form = EmployeeForm(initial=emp.__dict__)
        return render(request, "edit.html", {"form": form})
    

    # 