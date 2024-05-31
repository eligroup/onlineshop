from products.models import Product

class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session # request.user , request.session is different for each user
        cart=self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

            # self.session['cart'] = {}
            # cart=self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        add new product or another previous product to cart .
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:# it is related to add quantity on product page or update qty on cart page
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """
        save is a method after calling this method information in cart will be saved in session.
        modified is an attribute of session and says session is changed now you update it for user.
        after each change in cart we have to save it
        """
        self.session.modified = True

    def __iter__(self):
        """for making loop on part of cart ,get product.id and give us product detail from database
         and place product_obj as a key of product.id """
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in=product_id) # {2,15,32}
        cart = self.cart.copy() # make a copy from cart for doing operation on it

        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            yield item

    def __len__(self):
        """we can count all product in cart"""
        return len(self.cart.keys())

    def clear(self):
        """ we should empty cart through session"""
        del self.session['cart']
        self.save()

    def get_total_price(self):
        """get product.id then access to product by its id then sum all of them"""
        product_id = self.cart.keys() # {"1","2","3"}
        products = Product.objects.filter(id__in=product_id)
        return sum(product.price for product in products)
