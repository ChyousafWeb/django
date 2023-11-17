from django.shortcuts import render, HttpResponse ,redirect
from datetime import datetime
from ProjectApp.models import Contact
from ProjectApp.models import Signup
from ProjectApp.models import login
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request, 'index.html')

def back(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
 
def shop(request):
    return render(request,'shop.html')

def vagetables(request):
    return render(request,'vagetables.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def Signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password1')
        data = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        data.save()
        return redirect('home')
    return render(request, 'Signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
            
    return render(request,'login.html')