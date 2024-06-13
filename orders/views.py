from django.shortcuts import render
from django.http import HttpResponse


def order_create_view(request):
    return render(request, 'orders/order_create.html')


# Create your views here.
