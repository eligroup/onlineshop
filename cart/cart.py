from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _

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
        messages.success(self.request,_('product successfully add to cart' ))
        self.save()

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('product successfully removed from cart'))
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
        for item in cart.values():# key is product id and value is product-obj and qty
            item['total_price']=item['product_obj'].price * item['quantity'] # price is an attribute of modlel so for accessing we write .price
            yield item

    def __len__(self):
        """we can count all product in cart"""
        return sum(item['quantity'] for item in self.cart.values())
               

    def clear(self):
        """ we should empty cart through session"""
        del self.session['cart']
        self.save()


    def get_total_price(self):
        """get product.id then access to product by its id then sum all of them"""
        products= self.cart.values() # {"1","2","3"}
        return sum(item['quantity'] * item['product_obj'].price for item in products)

    def is_empty(self): # this method says if cart id empty in template not show go to cart buttond
        if self.cart:
            return False
        else:
            return True

        #products = Product.objects.filter(id__in=product_id)

        # count =0
        # for item in self.cart.values():
        #     count+=(item['total_price'])
        # return count
        # products = Product.objects.filter(id__in=product_id)


