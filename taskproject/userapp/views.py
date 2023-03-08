from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]  
        # check if the password is empty or 
        if username == "" or password == "" or repassword == "":
            messages.warning(request, "Please fill out all required fields")
            return redirect("/register")
        else:
            if password == repassword:
                # checking if the user is already exist
                if User.objects.filter(username = username).exists():
                    messages.warning(request, "This username already exists")
                    return redirect("/register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        password= password
                    )
                    user.save()
                    messages.success(request, "New username is created successfully ")
                    return redirect("/register")
                
            else:
                messages.warning(request,"Password don't match" )
                return redirect ("/register")
                
    else:       
        return render(request, "register.html")
    
    

def login(request):
    # check if any information/data is being request on the form
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        if username == "" or password == "":
            messages.warning(request, "Please fill out all required field")
            return redirect("/login")
        else:
            # login to the system
           user = auth.authenticate(username=username, password=password)
           if user is not None: #it means if the user exist in the system
               auth.login(request,user)
               return redirect("/")
           else:
               messages.warning(request, "This username does not exist")
               return redirect("/login")
            
    else :  
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/login")

    