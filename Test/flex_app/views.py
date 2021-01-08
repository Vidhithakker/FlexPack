from django.contrib import messages
from django.contrib.auth import authenticate
from .models import User
from django.shortcuts import render, redirect
from passlib.hash import pbkdf2_sha256

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def registerPage(request):
    if request.method=='POST':
        user_name = request.POST.get('username')
        name=request.POST.get('name')
        email= request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create()
        user.user_name=user_name
        user.name = name
        user.email=email
        user.password=pbkdf2_sha256.hash(password)


        user.save()

        print("User Created")
        return redirect('index')
    else:
        return render(request, 'register.html')


def loginPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, user_name=user_name, password=password)

    context = {}
    return render(request, 'login.html', context)
