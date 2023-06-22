from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

    
def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())
def join(request):
    template = loader.get_template('join.html')
    return HttpResponse(template.render())

def adduser(request):
     if request.method == "POST":
         customername=request.POST["fname"]
         customermail=request.POST["mail"]
         customerphone=request.POST["phone"]
         customerpassword=request.POST["psword"]
         myuser=User.objects.create_user(customername,customermail,customerpassword)
         myuser.save()
         return redirect("login")
     return render (request,'login.html')

def bookings(request):
    template = loader.get_template('booke.html')
    return HttpResponse(template.render())

def biryani(request):
    products=Food.objects.all()
    template = loader.get_template('biryani.html')
    return render(request,"biryani.html",{"Foods":products})


def test(request): 
    mydata=datastore.objects.all()
    if(mydata!=""):
       return render(request,"test.html",{"datas":mydata})
    else:
        return render(request,"test.html") 

def addData(request):
    if request.method=="POST":
            Firstname=request.POST["fname"]
            Lastname=request.POST["lname"]
            person=request.POST["personno"]
            phonenumb=request.POST["phonenumb"]
          
            date=request.POST["dates"]
            time=request.POST["times" ]

            obj=datastore()
            obj.First_name1=Firstname
            obj.Last_name1=Lastname
            obj.NO_of_persons1=person
            obj.phone_number1=phonenumb
           
            obj.Date1=date
            obj.Time1=time
            obj.save()
            mydata=datastore.objects.all()
            return redirect("test")
    return render(request,"test.html")

def login(request):
        template=loader.get_template('login.html')
        return HttpResponse(template.render())
    
def useraccess(request):
        if request.method == "POST":
            name=request.POST['name']
            pswd=request.POST['pswd']

            user=authenticate(username=name,password=pswd)
            if user is not None:
                return render(request,"index.html")
            else:
                return redirect("login")
        return render(request,"login.html")
        




