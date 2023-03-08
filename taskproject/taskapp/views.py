from django.shortcuts import render, redirect
from django.http import HttpResponse
from taskapp.models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login") # If the user isn't logged in, redirect to settings.LOGIN_URL , passing the current absolute path in the query string
def index(request):
    if request.method == "POST":
        # pulling data from the form
        name = request.POST["name"]
        # check if the value in the form is empty
        if name == "":
            messages.warning(request, "Please enter your new task")    
            return redirect("/")
        else:   
            # save the data and render it on the website
            task = Task.objects.create(name = name, manager = request.user)
            task.save
            messages.success(request, "New task has been added")
            return redirect("/")
            
    else:        
        all_task = Task.objects.filter(manager = request.user)
        # paginator
        page = request.GET.get("page")
        paginator = Paginator(all_task, 5)
        all_task = paginator.get_page(page)
        return render(request, "index.html", {"all_task": all_task})
    
    
@login_required(login_url="/login")  # If the user isn't logged in, redirect to settings.LOGIN_URL , passing the current absolute path in the query string
def complete_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    if task.manager == request.user:
        task.status = True
        task.save()
        return redirect("/")
    else:
        messages.success(request, "You have no authority to change this task") 
        return redirect("/")
        
    


@login_required(login_url="/login")# If the user isn't logged in, redirect to settings.LOGIN_URL , passing the current absolute path in the query string
def pending_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    if task.manager == request.user:
        task.status = False
        task.save()
        return redirect("/")
    else:
        messages.success(request, "You have no authority to change this task") 
        return redirect("/")

def delete(request, task_id):
    task = Task.objects.get(id = task_id)
    if task.manager == request.user:
        task.delete()
        return redirect("/")
    else:
        messages.success(request, "You have no authority to change this task")
        return redirect("/")
