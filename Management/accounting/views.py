from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accounting(request):
    return HttpResponse("Yey its accounting!!")