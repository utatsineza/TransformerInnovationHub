class Cart():

    def __init__(self, request):
        self.session = request.session

        # get the current session key
        cart = self.session.get('session_key')

        # for new users
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            # same as
            # self.session['session_key'] = {}
            # cart = self.session['session_key]

        # making cart available on all pages
        self.cart = cart
        