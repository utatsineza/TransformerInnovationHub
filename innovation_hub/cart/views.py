from django.shortcuts import render, get_object_or_404, HttpResponse
from .cart import Cart
from webstore.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)

    cart_products = cart.get_prods()
    return render(request, "cart.html", {"cart_products": cart_products})



def cart_add(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = request.POST.get("product_id")

        if not product_id:
            print("Got an empty string!")
            return HttpResponse("Got empty string")

        product_id = int(product_id)

        # Get product from DB
        product = get_object_or_404(Product, id=product_id)

        # Add product to cart
        cart.add(product)

        # Get the updated cart quantity
        cart_quantity = len(cart)

        # Send updated cart quantity as a JSON response
        return JsonResponse({"qty": cart_quantity})

def cart_delete(request):
    pass


def cart_update(request):
    pass
