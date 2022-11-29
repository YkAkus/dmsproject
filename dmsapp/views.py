from django.shortcuts import render
from django.contrib.auth import login, authenticate
from importlib.metadata import requires
from dmsapp.models import registers

def login(request):
    return render(request,'login.html')
            
def index(request):
    return render(request,'index.html')
    # if request.method=="POST":
    #     email=request.POST.get("email")
    #     password=request.POST.get("password")
    #     if email!="" and password !="":
    #         user=authenticate(email=email,password=password)
    #         if user is not None:
    #             login(request,'index.html')
    #         else:
    #             return render(request,'login.html',{'error': 'Wrong username!!!'})
def forgot(request):
    return render(request,'forgot-password.html')
def createlog(request):
    return render(request,'register.html')
def reg(request):
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        regus=registers(fname=fname,lname=lname,email=email,password=password)
        regus.save()
    return render(request,'login.html')
def table(request):
    return render(request,'tables.html')
def chart(request):
    return render(request,'charts.html')