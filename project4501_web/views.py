from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product(request, pk = ''):
    return render(request, 'product.html')