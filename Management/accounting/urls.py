from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers, name = 'acc'),
    path('orders/', views.orders, name = 'orders'),
    path('products/', views.products, name = 'products'),

]