from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json
from .forms import SignupForm, LoginForm, ListingForm
# make a GET request and parse the returned JSON                                                                                                                                                           # note, no timeouts, error handling or all the other things needed to do this for real                                                                                                                      

#Notes: currently no timeouts, error handling or all the other things needed to do this for real                                                                                                                      

#Home: currently no service-oriented home page 
def home(request):
    return render(request, 'home.html')

#Course-GET: Use course service to get information of a course
def course_info(request, pk = ''):
    #Method1 with requests:
    course_req = requests.get('http://exp-api:8000/v1/course/'+pk)
    course = json.loads(course_req.text)
    return render(request, 'course_info.html', course)
    #Method2 with urllib:
    # req = urllib.request.Request('http://exp-api:8000/course/'+pk)
    # resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    # resp = json.loads(resp_json)
    # context_dict = resp
    # return render(request, 'course_info.html', context_dict)

#Courses-GET: Use courses service to get information of all courses
#Notes: may need to change to base on search options
def courses_info(request):
    courses_req = requests.get('http://exp-api:8000/v1/courses/')
    courses = json.loads(courses_req.text)
    return render(request, 'courses_info.html', {'courses': courses})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        #if form.is_valid():
            #Process and clean data 
            #Redirect to new URL

    #urllib.request.Request('http://exp-api:8000/product'+info)
    else: 
        form = SignupForm()
    #Temporarily using login.html to render
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'GET':
        #Not sure if it's okay to do None here
        form = LoginForm(request.GET or None)
        #if form.is_valid():
            #Process and clean data 
            #Redirect to new URL
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def listing(request):
    if request.method == 'POST':
        form = LisingForm(request.POST)
        #if form.is_valid():
            #Process and clean data 
            #Redirect to new URL
    else:
        form = ListingForm()

    #Temporarily using login.html to render
    return render(request, 'listing.html', {'form': form})


def logout(request):
    #Check this with group
    #if request.method == 'DELETE':
    #    form = LisingForm(request.DELETE)
        #if form.is_valid():
            #Process and clean data 
            #Redirect to new URL
    #else:
    #    form = ListingForm()
    #Temporarily using login.html to render
    return render(request, 'logout.html')


    