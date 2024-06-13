from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Order(models.Model):
    #user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name=_('user')) # 1 way of accessing user
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,verbose_name=_('user'), on_delete=models.CASCADE ) # 2 way of accessing user
    is_paid=models.BooleanField(_('is paid'),default=False)

    first_name = models.CharField(_('first name'),max_length=100)
    last_name = models.CharField(_('last name'),max_length=200)
    phone_number = models.CharField(_('phone number'),max_length=12, )
    address = models.CharField(_('address'),max_length=700)
    order_notes = models.CharField(_('notes'),max_length=700, blank=True)

    datetime_created = models.DateTimeField(_('date created'),auto_now_add=True)
    datetime_modified = models.DateTimeField(_('date modified'),auto_now=True)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = _('orders')

    def __str__(self):
        return f'order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='items', verbose_name=_("order"))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items' , verbose_name=_('product name'))
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField() # we should save the price in database for knowing the history of product price but in cart price should be upgared
    class Meta:
        verbose_name = "order item"
        verbose_name_plural = _('order items')

    def __str__(self):
        return f'order item {self.id}|product:{self.product} x {self.quantity}| price:{self.price}'


# Create your models here.
