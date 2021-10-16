from django.contrib.messages.api import error
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as user_login, logout as logout_user
from django.contrib import messages
from django.contrib.auth.models import User
from .regex import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        if request.POST['filteration'] == "1":
            txt = request.POST['txt']
            ans = find_numbers(txt)
        if request.POST['filteration'] == "2":
            txt = request.POST['txt']
            ans = extract_date(txt)
        elif request.POST['filteration'] == "3":
            txt = request.POST['txt']
            ans = extract_quotes(txt)
        elif request.POST['filteration'] == "4":
            txt = request.POST['txt']
            ans = []
            if is_email_valid(txt):
                ans.append(f"{txt} is a valid email")
            else:
                ans.append(f"{txt} is a invalid email")
        elif request.POST['filteration'] == "5":
            txt = request.POST['txt']
            ans = is_ip_valid(txt)
        elif request.POST['filteration'] == "6":
            txt = request.POST['txt']
            ans = []
            if is_mac_valid(txt):
                ans.append(f"{txt} is a valid MAC address")
            else:
                ans.append(f"{txt} is a invalid MAC address")
        elif request.POST['filteration'] == "7":
            txt = request.POST['txt']
            ans = CamelTo_snake(txt)
        context = {'ans':ans, 'txt':txt}
        return render(request, "home/home.html", context)   
    return render(request, "home/home.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        error_count = 0
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken.")
            error_count += 1
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            error_count += 1
        if not is_email_valid(email):
            messages.error(request, "Enter a Valid email.")
            error_count += 1
        if not password1 == password2:
            messages.error(request, "Passwords not matching.")
            error_count += 1

        if error_count == 0:
            user = User.objects.create_user(username, email, password1)
            name_list = name.split()
            user.first_name = name_list[0]
            user.last_name = name_list[1]
            user.save()
            messages.success(request, f"Account created for {name}")
            return redirect('home')
    return render(request, "home/register.html")
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username = username, password = password)
        if user is not None:
            user_login(request, user)
            messages.success(request, 'Login Succesful')
            return redirect('home')
            
        else:
            messages.error(request, 'Invalid Credentials')


    return render(request, "home/login.html")

def logout(request):
    logout_user(request)
    print(request.user.is_authenticated)
    messages.info(request, "Logged Out.")
    return redirect(reverse('home'))
    

