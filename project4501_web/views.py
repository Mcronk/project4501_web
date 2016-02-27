from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# make a GET request and parse the returned JSON                                                                                                                                                           # note, no timeouts, error handling or all the other things needed to do this for real                                                                                                                      



def index(request):
    return render(request, 'index.html')

def product(request, pk = ''):
    return render(request, 'product.html')

    