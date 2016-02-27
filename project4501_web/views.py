from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# make a GET request and parse the returned JSON                                                                                                                                                           # note, no timeouts, error handling or all the other things needed to do this for real                                                                                                                      

def index(request):
	return render(request, 'index.html')

def product(request, pk = ''):
	req = urllib.request.Request('http://exp-api:8000/product')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	context_dict = resp 
	return render(request, 'product.html', context_dict)

	