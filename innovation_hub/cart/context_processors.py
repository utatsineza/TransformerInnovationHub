from .cart import Cart


# creating context processor
def cart(request):

    # return the default data from the cart
    return {"cart": Cart(request)}
