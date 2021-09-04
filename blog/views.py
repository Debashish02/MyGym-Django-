from django.shortcuts import render
from . import views
from .models import Contact

# Create your views here.
def blog(request):
    return render(request,"blog/index.html")

def create_contact(request):
    if request.method =="POST":
        
        email = request.POST['email']
        name = request.POST['name']
        mobile = request.POST['mobile']
        message = request.POST['message']
        # print(email, name,mobile,message)
        contact = Contact(email=email,name=name,mobile=mobile)
        contact.save()
        print('the data is loading')

    return render(request,"blog/contact.html")

def about(request):
    return render(request,"blog/about-us.html")

def login(request):
    return render(request,"blog/login.html")

def contact(request):
    return render(request,"blog/contact.html")

