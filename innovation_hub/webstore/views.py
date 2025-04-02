from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    return render(request, "home.html")


def store(request):
    products = Product.objects.all()
    return render(request, "shop.html", {'products': products})


def product(request):
    return render(request, "single-product.html")


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

def login(request):
    return render(request, "sign-in.html")


def signup(request):
    return render(request, "sign-up.html")

def layout(request):
    return render(request, 'layout.html')