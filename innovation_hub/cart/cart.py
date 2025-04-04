from webstore.models import Product
class Cart():

    def __init__(self, request):
        self.session = request.session

        # Initialize cart if it doesn't exist
        if 'session_key' not in self.session:
            self.session['session_key'] = {}

        # Now that the session key exists, get the cart from session
        self.cart = self.session['session_key']

    def add(self, product):
        product_id = str(product.id)

        # Add product to cart if not already there
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        # Mark session as modified
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get ids from cart
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        # returning products in cart
        return products
