from webstore.models import Product
class Cart():

    def __init__(self, request):
        self.session = request.session

        # Initialize cart if it doesn't exist
        if 'session_key' not in self.session:
            self.session['session_key'] = {}

        # Now that the session key exists, get the cart from session
        self.cart = self.session['session_key']

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Add product to cart if not already there
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

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

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # update cart
        store_cart = self.cart
        store_cart[product_id] = product_qty

        self.session.modified = True
        new_cart = self.cart
        return new_cart

    def delete(self, product):
        product_id = str(product)

        # delete product from dictionary
        if product in self.cart:
            del self.cart[product_id]

        self.session.modified = True