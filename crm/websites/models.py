
from distutils import dep_util
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
    customerName = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    organizationName = models.CharField(max_length=200, null=True)
    jobTitle = models.CharField(max_length=200, null=True)
    customerCategory = models.CharField(max_length=200, null=True)
    customerPhonenumber = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    postcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customerName



class Product_Category(models.Model):
    
    categoryName = models.CharField(max_length=200, null = True)
    Description = models.CharField(max_length=1000, null = True)
    def __str__(self):
        return self.categoryName


class Product(models.Model):

    categoryId = models.ForeignKey(Product_Category, models.SET_NULL, blank=True,null=True,)
    productName = models.CharField(max_length=200, null=True)
    productPrice = models.FloatField(default=0)
    stockQuantity = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add = True, null = True)
    def __str__(self):
        return self.productName


status = (
    ("Pending", "Pending"),
    ("Delivered", "Delivered"),
    ("Completed", "Completed"),
    ("Declined", "Declined"),
)

class Order(models.Model):

    customerName = models.ForeignKey("Customer", models.SET_NULL,
    blank=True, null=True,)
    productName = models.ForeignKey("Product", models.SET_NULL,
    blank=True, null=True,)
    productQuantity = models.IntegerField(default=0)
    ordered_at = models.DateTimeField(auto_now_add = True, null = True)
    orderStatus = models.CharField(max_length = 100, choices = status, default="Pending")

    def __str__(self):
        return f"OrderedID: {self.id}, CustomerName: {self.customerName}, OrderedProduct: {self.productName}"

ways = (
    ("None", "None"),
    ("Cash", "Cash"),
    ("MobileBanking", "MobileBanking"),
    ("Banking", "Banking"),
)

class Payment(models.Model):

    orderId = models.ForeignKey("Order", models.SET_NULL,
    blank=True, null=True,)
    paidAmount = models.FloatField(default=0)
    paymentAt = models.DateTimeField(auto_now_add = True, null = True)
    paymentWay = models.CharField(max_length= 100, choices=ways, default="None")

    def __str__(self):
        return f"PaymentID: {self.id}, OrderedID: {self.orderId.id}, CustomerName: {self.orderId.customerName}, PaidAmount: {self.paidAmount} TK"