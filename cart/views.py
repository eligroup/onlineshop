from django.shortcuts import render , get_object_or_404 , redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import AddProductToCart
from products.models import Product



def cart_detail_view(request):
    cart = Cart(request) # we sent request to cart and get session ,request and cart
    for item in cart:
        item['product_item_quantity_form']=AddProductToCart(initial={'quantity':item['quantity'],
                                                                     'inplace':True
                                                                     })
    return render(request,'cart/cart_detail.html',{"cart":cart}) # as context we sent cart

@require_POST
def add_to_cart_view(request ,product_id): # we get request an product_id
    """ this view when is called that user click on 'add to card' on  product_detail.html and we should fill the form
    by sent information by user"""
    cart = Cart(request) # if before we had sth in session for user now we can access it by this code
    product = get_object_or_404(Product, id=product_id) # we should check if we have this product or no
    form = AddProductToCart(request.POST) # fill the form by this code
    if form.is_valid():
        cleaned_data = form.cleaned_data # get information from cleaned data
        quantity = cleaned_data['quantity']
        cart.add(product , quantity, replace_current_quantity=cleaned_data['inplace']) # now we should say add product
        # and quantity to cart. we do this with add method of cart.py.
    return redirect("cart:cart_detail") # here cart is app name defined in urls.py

def remove_from_cart_view(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")

@require_POST
def empty_cart(request):
    cart=Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")




# Create your views here.
