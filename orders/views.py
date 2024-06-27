from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from .forms import OrderForm, OrderItem
from django.utils.translation import gettext as _
from django.http import HttpResponse


@login_required
def order_create_view(request):
    order_form = OrderForm() #although we used of our html form but as errors saved in form we send this form to context.
    cart = Cart(request) # for getting data of cart we should access to cart includes

    if len(cart)==0:
        messages.warning(request,_("your cart is empty.you can not proceed to checkout."))
        return redirect('product_list')
     #make order
    if request.method == "POST": # if the form sent
        order_form = OrderForm(request.POST) #save whatever has written in form
         # save order in database
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)# save form but not in database because it dosent have user
            order_obj.user = request.user
            order_obj.save()
            # save order items in database
            for item in cart: # for adding cart items to order item we need a loop that iterate on cart item.
                product = item['product_obj'] # fisrt we get each product
                OrderItem.objects.create( # make an obj of orderitems and complete its item
                    order=order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price
                )
            # clear cart
            cart.clear() #at the end of process we should clear the cart

            request.user.first_name = order_obj.first_name #for saving fname and lname in database request user
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id       #for accessin to order id in payment app we have to save id in session
            return redirect('payment:payment_process')

            # messages.success(request, _("your order has successfully placed."))
    return render(request, 'orders/order_create.html',context={"form":order_form}) # as we used our html form it is not necessary to send form :context = {'form': OrderForm()})


# Create your views here.
