from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages


# Create your views here.
def demo(request):
    return HttpResponse("<h1> Hello world! This is demo of HttpResponse <h1>")

def index(request):
    all_person = Person.objects.all
    return render(request, "index.html", {"all_person":all_person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        # receive the data
        name = request.POST["name"]
        age =  request.POST["age"]
        # save the data
        person = Person.objects.create(
            name = name,
            age = age
        )
        person.save()
        messages.success(request, "Successfully saved")
        
        # change direction of the page 
        return redirect("/")       
    else:  
        return render(request, "form.html")
    
def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id = person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "Data has been successfully updated")
        return redirect("/")       

    else:
        # data wants to be edited
        person = Person.objects.get(id = person_id)
        return render(request, "edit.html", {"person": person})


def delete(request, person_id):
        person = Person.objects.get(id = person_id)
        person.delete()
        messages.success(request, "Data has been successfully deleted")
        return redirect("/")
        