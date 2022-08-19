from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name = "dashboard"),
   path('customers/', views.customer, name = "customer"),
   path('products/', views.product, name = "product"),
   path('orders/', views.order, name = "order"),
   path('categories/', views.product_category, name = "category"),
   path('payments/', views.payment, name = "payment"),
   
]