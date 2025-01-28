from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request, "home/index.html", {"show_nav": True})
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, "home/register.html", {"form": form, "show_nav": False})
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, "home/login.html", {"form": form, "show_nav": False})

def logout_view(request):
    logout(request)
    return redirect("home")