from django.urls import path
from . import views

app_name = "webstore"
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("shop", views.store, name="shop"),
    path("checkout", views.checkout, name="checkout"),
    path("cart", views.cart, name="cart"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("register", views.register_user, name="register_user"),
    path("product/<int:pk>", views.product, name="product"),
]
