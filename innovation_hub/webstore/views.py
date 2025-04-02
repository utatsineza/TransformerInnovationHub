from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def home(request):
    return render(request, "home.html")


def store(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "single-product.html", {'product': product})


def cart(request):
    return render(request, "cart.html")


def blog(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def checkout(request):
    return render(request, "checkout.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged in")
            return redirect("webstore:home")
        else:
            messages.success(request, "Oops! Failed to log you in")
            return redirect("webstore:login_user")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    # messages.success(request, "You have been logged out, Thanks for shopping with us")
    return redirect("webstore:home")


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, "registered succesffuly")
            return redirect("webstore:home")
        else:
            messages.success(request, "Oops there was problem registerring try again")
            return redirect('webstore:register_user')
            # print(form.errors)
    else:
        return render(request, "register.html", {'form': form})

