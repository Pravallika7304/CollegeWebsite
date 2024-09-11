from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Register,Contactus
def index(request):
    #return HttpResponse("This is index view response")
    return render(request,'index.html')
def about(request):
    #return HttpResponse("This is about view response")
    return render(request,'about.html')
def placements(request):
    #return HttpResponse("This is about view response")
    return render(request,'placements.html')
def register(request):
    #return HttpResponse("This is brief view response")
    return render(request,'register.html')
def modify(request):
    operation=request.GET['operation']
    FullName=request.GET['FullName']
    Email=request.GET['Email']
    Password=request.GET['Password']
    GraduationYear=request.GET['GraduationYear']
    PhoneNo=request.GET['PhoneNo']
    desig=request.GET['desig']
    r=Register.objects.get(Email=Email)
    if operation=="update":
        r.FullName=FullName
        r.Email=Email
        r.Password=Password
        r.GraduationYear=GraduationYear
        r.PhoneNo=PhoneNo
        r.desig=desig
        r.save()
    else:
        Register.delete(r)
    users=Register.objects.all()
    return render(request,'viewusers.html',{"users":users})
def doregister(request):
    FullName=request.GET['FullName']
    Email=request.GET['Email']
    Password=request.GET['Password']
    GraduationYear=request.GET['GraduationYear']
    PhoneNo=request.GET['PhoneNo']
    r=Register()
    r.FullName=FullName
    r.Email=Email
    r.Password=Password
    r.GraduationYear=GraduationYear
    r.PhoneNo=PhoneNo
    r.save()
    return render(request,'register.html',{"msg":"Registration Successfull"})
def login(request):
    #return HttpResponse("This is brief view response")
    return render(request,'login.html')
def contactus(request):
    #return HttpResponse("This is brief view response")
    return render(request,'contactus.html')
def logincheck(request):
    Email=request.GET['Email']
    Password=request.GET['Password']
    try:
        r=Register.objects.get(Email=Email,Password=Password)
    except Exception as ex:
        return render(request,'login.html',{"msg":"Invalid email/password"})
    return render(request,'more.html',{"msg":"You have successfully logged in"})
def docontact(request):
    #return HttpResponse("This is brief view response")
    Name=request.GET['Name']
    Email=request.GET['Email']
    Subject=request.GET['Subject']
    Message=request.GET['Message']
    r=Contactus()
    r.Name=Name
    r.Email=Email
    r.Subject=Subject
    r.Message=Message
    r.save()
    r=Contactus.objects.get(Name=Name,Email=Email,Subject=Subject,Message=Message)
    return render(request,'thanku.html',{"msg":"Thankyou for contacting us"})
def userhome(request):
    return render(request,'user.html')
def adminhome(request):
    return render(request,'adminhome.html')
def viewusers(request):
    return render(request,'viewusers.html')
def viewusers(request):
    user=Register.objects.all()
    return render(request,'viewusers.html',{"users":user})
def more(request):
    return render(request,'more.html')