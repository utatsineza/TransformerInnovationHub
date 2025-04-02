from django.urls import path
from . import views

app_name = "webstore"
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("shop", views.store, name="shop"),
    path("product", views.product, name="product"),
    path("cart", views.cart, name="cart"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("checkout", views.checkout, name="checkout"),
    path("layout", views.layout, name="layout")
]
