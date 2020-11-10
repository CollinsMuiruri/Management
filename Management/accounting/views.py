from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def accounting(request):

    customers = Customer.objects.all()

    return render(request, 'home.html', {'customers': customers})