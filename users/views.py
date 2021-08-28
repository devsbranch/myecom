from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def Home_page(request):
    return render(request, 'userstemp.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(first_name,last_name,username,email,password)

        User.objects.create_user(username=username,password=password, email=email, first_name=first_name,last_name=last_name)

        print('save')
    else:
     return render(request, 'register.html')


def login(request):
    pass
