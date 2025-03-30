from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def store(request):
    return render(request, "store.html")


def product(request):
    return render(request, "single-product.html")


def cart(request):
    return render(request, "cart.hml")


def blog(request):
    return render(request, "blog.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def checkout(request):
    return render(request, "checkout.html")

def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "sign-up.html")
