import requests
import json
from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.http import HttpResponse
from orders.models import Order
from django.conf import settings


def payment_process(request):
    # get order id from session
    order_id = request.session.get('order_id') #from session we get order id
    # get order odject from database
    order=get_object_or_404(Order,id=order_id) #check if order id exist and we fetch data in order

    toman_total_price = order.get_total_price() #now we get total price in toman and rial
    rial_total_price = toman_total_price*10

    zarinpal_request_url="url defined by zarinpal"

    request_header={ #what send and receive should be jason /each request has body and header
        "accept":"application/json",
        "content-type": "application/jason"
    }
    request_data ={
        'merchant_id':settings.ZARINPAL_MERCHANT_ID,
        'amount':rial_total_price,
        'description':f'#{order.id}{order.user.first_name}{toman_total_price}',
        'callback_url':'http://127.0.0.1:8000'+reverse('payment:payment_callback'),  #our url address
    }
    res=requests.post(url=zarinpal_request_url,data=json.dumps(request_data),headers=request_header) # send a post request to "url" with this information /
    # we should change dictionary yo jason: a format for transfering data / header is another parameter we should send
    #after sending information we receive a response put it in res
    data = res.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not  in data or len(data['errors'])==0:
        return redirect('https://www.zarinpal.com/{authority}'.format(authority=authority))
    else:
        return HttpResponse("errors from zarinpal")


def payment_callback(request):
    payment_authority=request.GET.get('Authority')
    payment_status=request.GET.get('Status')
    order=get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()  # now we get total price in toman and rial
    rial_total_price = toman_total_price * 10
    if payment_status=="OK":
        request_header = {  # what send and receive should be jason /each request has body and header
            "accept": "application/json",
            "content-type": "application/jason"
        }
        request_data = {
            'merchant_id': settings.ZARINPAL_MERCHANT_ID,
            'amount': rial_total_price,
            'authority':payment_authority
        }
        res = requests.post(url=zarinpal_callbak_payment_url, data=json.dumps(request_data), headers=request_header)

        if 'data' in res.json() and (len(res.json()['data']['errors'])==0 or 'errors' not in res.json()['data']):
            data = res.json()['data']
            payment_code = data['code'] # verify code return code and ref_id
            payment_ref_id = data['ref_id']

            if payment_code ==100:#everything is ok
                order.is_paid=True
                order.ref_id= payment_ref_id # we shold make a field in ordder
                order.zarinpal_data=data
                order.save()
                return HttpResponse("YOU PAID SUCCESSFELLY")
            elif payment_code==101:
                return HttpResponse("YOU PAID SUCCESSFELLY. tyour paid befor registered")

            else:
                errors_code=res.json()['errors']['code']
                errors_message=res.json()['errors']['message']
                return HttpResponse(f"your PAID is unsuccessful.{errors_message}{errors_code}")
    else:
        return HttpResponse(f'you paid unsuccessfully')


def payment_process_sandbox(request):
    # get order id from session
    order_id = request.session.get('order_id') #from session we get order id
    # get order odject from database
    order=get_object_or_404(Order,id=order_id) #check if order id exist and we fetch data in order

    toman_total_price = order.get_total_price() #now we get total price in toman and rial
    rial_total_price = toman_total_price*10

    zarinpal_request_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json'

    request_header={ #what send and receive should be jason /each request has body and header
        "accept":"application/json",
        "content-type": "application/json"
    }
    request_data ={
        'MerchantID':"ABCabcABCabcABCabcABCabcABCabcABCabc",
        'Amount':rial_total_price,
        'Description':f'#{order.id}{order.user.first_name}{toman_total_price}',
        'CallbackURL':request.build_absolute_uri(reverse('payment:payment_callback')),  #our url address
    }
    res=requests.post(url=zarinpal_request_url,data=json.dumps(request_data),headers=request_header) # send a post request to "url" with this information /
    # we should change dictionary yo jason: a format for transfering data / header is another parameter we should send
    #after sending information we receive a response put it in res
    data = res.json()
    authority = data['Authority']
    order.zarinpal_authority = authority
    order.save()
    print("data=",data)
    print("res=", res)

    if 'errors' not in data or len(data['errors'])==0:
        return redirect('https://sandbox.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse("errors from zarinpal")

def payment_callback_sandbox(request):
    payment_authority=request.GET.get('Authority')
    payment_status=request.GET.get('Status')
    order=get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()  # now we get total price in toman and rial
    rial_total_price = toman_total_price * 10
    if payment_status=="OK":
        request_header = {  # what send and receive should be jason /each request has body and header
            "accept": "application/json",
            "content-type": "application/json"
        }
        request_data = {
            'MerchantID': "ABCabcABCabcABCabcABCabcABCabcABCabc",
            'Amount': rial_total_price,
            'Authority':payment_authority
        }
        res = requests.post(
            url='https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json',
            data=json.dumps(request_data),
            headers=request_header)
        if 'errors' not in res.json():
            data = res.json()
            payment_code = data['Status'] # verify code return code and ref_id
            payment_ref_id = data['RefID']

            if payment_code ==100:#everything is ok
                order.is_paid=True
                order.ref_id= payment_ref_id # we shold make a field in ordder
                order.zarinpal_data=data
                order.save()
                return HttpResponse("YOU PAID SUCCESSFELLY")
            elif payment_code==101:
                return HttpResponse("YOU PAID SUCCESSFELLY. tyour paid befor registered")

            else:
                errors_code=res.json()['errors']['code']
                errors_message=res.json()['errors']['message']
                return HttpResponse(f"your PAID is unsuccessful.{errors_message}{errors_code}")
    else:
        return HttpResponse(f'you paid unsuccessfully')
