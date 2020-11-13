from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Order, Product

# Create your views here.
def customers(request):

    customers = Customer.objects.all()

    return render(request, 'home.html', {'customers': customers})

def orders(request):

    orders = Order.objects.all()

    return render(request, 'orders.html', {'orders': orders})

def products(request):

    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})