from django.contrib import admin
from .models import Order,OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):# admin.StackedInline : change the view of admin panel
    model = OrderItem
    fields = ['order','product' , 'quantity', 'price']
    extra = 1 # create an empty tab


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['user','first_name','last_name','datetime_created','is_paid']
    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','price']
    


# Register your models here.
