from ast import Or
from http.client import ImproperConnectionState
from typing import Final
from django.shortcuts import render
from .models import *
from django.db.models import Avg, Count, Min, Sum
# Create your views here.



def customer(request):

    customerInfoList = Customer.objects.all
    return render(request, 'websites/customer.html', {
        'customerList': customerInfoList
        })


def product(request):

    productList = Product.objects.all
    return render(request, 'websites/product.html', {
        'products': productList
    })

def product_category(request):

    categoryList = Product_Category.objects.all
    return render(request, 'websites/category.html', {
        'categoryList' : categoryList
    })


ordered_price_list = []
priceSum = [0]
def order(request):

    orderList = list(Order.objects.all())
    productList = list(Product.objects.all())
    myList = zip(orderList, productList)
    finalList = []
    price_sum = 0
    for i, j in myList:
        total = i.productQuantity * j.productPrice
        price_sum += total
        finalList.append(total)
        ordered_price_list.append(total)
    
    priceSum[0] = price_sum
    priceList = zip(orderList, finalList)

    return render(request, 'websites/order.html', {
        'orders': priceList
    })


def payment(request):

    order(request)
    dueAmount = []
    payment_list = list(Payment.objects.all())
    paymentZip = zip(payment_list, ordered_price_list)

    for i, j in paymentZip:
        due = j - i.paidAmount
        dueAmount.append(due)

    payments = zip(payment_list, dueAmount, ordered_price_list)
    return render(request, 'websites/payment.html', {
        'payments': payments
    })


def dashboard(request):

    order(request)
    totalOrders = Order.objects.count()
    totalDelivered = Order.objects.filter(orderStatus = "Delivered").count()
    totalPending = Order.objects.filter(orderStatus = "Pending").count()
    totalDeclined = Order.objects.filter(orderStatus = "Declined").count()
    totalCompleted = Order.objects.filter(orderStatus = "Declined").count()
    totalAmount = priceSum[0]
    totalPayment = list(Payment.objects.aggregate(Sum('paidAmount')).values())[0]
    totalDue = totalAmount - totalPayment
    totalProduct = Product.objects.count()

    return render(request, 'websites/index.html', {
        'totalOrders': totalOrders,
        'totalDelivered': totalDelivered,
        'totalPending': totalPending,
        'totalDeclined': totalDeclined,
        'totalCompleted': totalCompleted,
        'totalPayment': totalPayment,
        'totalAmount': totalAmount,
        'totalDue': totalDue,
        'totalProduct': totalProduct,
    })
