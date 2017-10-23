from django.shortcuts import render, redirect
from apps.log.models import users
def index(request):
    context={
        "users": users.objects.all()
    }
    return render(request,'login/index.html',context)
def create(request):
    return render(request,"login/create.html")
def add(request):
    users.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], age=request.POST['age'], email=request.POST['email'])
    return redirect("/")
def show(request):
    if request.GET["sort"]=="first":
        print(users.objects.first)
        return redirect("/")
    elif request.GET["sort"]=="last":
        print(users.objects.last)
        
        return redirect("/")
    elif request.GET["sort"]=="all":
        context={
            "message":users.objects.all
        }
        return redirect("/")
    elif request.GET["sort"]=="alpha":
        return redirect("/")
    elif request.GET["sort"]=="create":
        return redirect("/create")
# Create your views here.
