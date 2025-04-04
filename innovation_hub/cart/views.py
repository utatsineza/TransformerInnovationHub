from django.shortcuts import render, get_object_or_404, HttpResponse
from .cart import Cart
from webstore.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)

    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(
        request, "cart.html", {"cart_products": cart_products, "quantities": quantities}
    )


def cart_add(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = request.POST.get("product_id")
        product_qty = request.POST.get("product_qty")

        if not product_qty:
            print("Got an empty string!")
            return HttpResponse("Got empty string")

        # product_id = int(product_id)
        # product_qty = int(product_qty)
        # Get product from DB
        product = get_object_or_404(Product, id=product_id)

        # Add product to cart
        cart.add(product=product, quantity=product_qty)

        # Get the updated cart quantity
        cart_quantity = cart.__len__()

        # Send updated cart quantity as a JSON response
        return JsonResponse({"qty": cart_quantity})


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = request.POST.get("product_id")

        # calling the delete function
        cart.delete(product=product_id)

        response = JsonResponse({"product": product_id})
        return response
        return redirect("cart_summary")

def cart_update(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = request.POST.get("product_id")
        product_qty = request.POST.get("product_qty")

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({"qty": product_qty})
        return response
        return redirect("cart_summary")
