from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json, requests

# make a GET request and parse the returned JSON                                                                                                                                                           # note, no timeouts, error handling or all the other things needed to do this for real                                                                                                                      

def home(request):
	return render(request, 'home.html')

def course_info(request, pk = ''):
	# course_req = requests.get('http://exp-api:8000/courses/'+course_pk)
	req = urllib.request.Request('http://exp-api:8000/course/'+pk)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	context_dict = resp
	context_dict2 = {'name': 'vainglory', 'tutor': 'johnson', 'price': '333', 'description': 'Teach you how to be a master in vainglory in three classes, each with 60 minutes.'}
	return render(request, 'course_info.html', context_dict)

def courseList(request):
	course_req = requests.get('http://exp-api:8000/courses/')
	courseList = json.loads(course_req.text)
	return render(request, 'courseList.html', {'courseList': courseList})
	#req = urllib.request.Request('http://exp-api:8000/courseList'+pk)
	#resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	#resp = json.loads(resp_json)

	#context_dict = resp
	courseList = [{'name': '3', 'course_tutor': 'j', 'price': '3', 'description': '.'}, {'name': '3', 'course_tutor': 'j', 'price': '3', 'description': '.'}]
	return render(request, 'courseList.html', {'courseList': courseList})

	return render(request, 'courseList.html', context_dict)

	