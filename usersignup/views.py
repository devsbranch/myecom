from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def registration(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully registered.")
            return redirect(reverse('registers'))
    else:
        form = CreateUserForm()
        messages.error(request, "enter the valid information")
    return render(request, template_name="register.html", context={'register_form': form})


def loginuser(request):
    form = AuthenticationForm
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are logged in as {username}")
                return
            else:
                messages.error(request, "invalid username or password")
        else:
            form = AuthenticationForm()
            messages.error(request, " invalid user name or password")
    return render(request,template_name="login.html", context={'login_form': form})



def logoutuser(request):
    logout(request)
    messages.info(request, "user logout")
    return render(request, template_name="logout.html")
