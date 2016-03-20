from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json
import requests
from django.core.urlresolvers import reverse
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
        if not form.is_valid():
            return render(request, 'signup.html', {'form':form, 'error':'Please complete the form correctly'})
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']
            data = {'name': name, 'password':password, 'email':email, 'phone':phone, 'description':description}          
            response = requests.post('http://exp-api:8000/v1/create_account/', data = data)
            response_data = json.loads(response.text)
            return JsonResponse({'result': response_data}, safe=False)
    #urllib.request.Request('http://exp-api:8000/product'+info)
    else: 
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    # if request.method == 'GET':
    #     form = LoginForm()
    #     next = request.GET.get('next') or reverse('home')
    #     return render(request,'login.html', {'form':form})
    # form = LoginForm(request.POST)
    # if not form.is_valid():
    #     return render(request, 'login.html', {'form':form, 'error':'The username and password you entered did not match our records. Please double-check and try again.'})
    # email = form.cleaned_data['email']
    # password = form.cleaned_data['password']
    # next = f.cleaned_data.get('next') or reverse('home')
    # #resp = login_exp_api ()
    # if not resp or not resp['work']:
    #   # couldn't log them in, send them back to login page with error
    #     return render(request, 'signup.html', {'form':form, 'error':'The username and password you entered did not match our records. Please double-check and try again.'})
    # authenticator = resp['resp']['authenticator']
    # response = HttpResponseRedirect(next)
    # response.set_cookie("auth", authenticator)
    # return response

    if request.method == 'GET':
       #Check... not sure if it's okay to do None here
       form = LoginForm(request.POST)
       if form.is_valid():
           # Process and clean data 
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           info = {'email': email, 'password':password}
           requests.get('http://exp-api:8000/v1/', info)
    else:
       form = LoginForm()
    return render(request, 'login.html', {'form': form})

def listing(request):
    # auth = request.COOKIES.get('auth')
    # if not auth:
    #     # handle user not logged in while trying to create a listing
    #     return HttpResponseRedirect(reverse("login") + "?next=" + reverse("listing")
    # if request.method == 'GET':
    #     form = ListingForm();
    #     return render("listing.html", {'form':form})
    # form = ListingForm(request.POST)
    # if not form.is_valid:
    #     form = ListingForm();
    #     return render("listing.html", {'form':form, 'error':'Please complete the form correctly'})
    # course_name = form.cleaned_data['course_name']
    # tag = form.cleaned_data['tag']
    # description = form.cleaned_data['description']
    # qualification = form.cleaned_data['qualification']
    # times = form.cleaned_data['times']
    # price = form.cleaned_data['price']
    # #resp = create_listing_exp_api ()
    # if resp and not resp['work']:        
    #     if resp['error'] == exp_srvc_errors.E_UNKNOWN_AUTH:
    #         # exp service reports invalid authenticator -- treat like user not logged in
    #         return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")
    # return render("listing.html", {'form':form, 'success', 'Your listing has been created.'})
    if request.method == 'POST':
       form = ListingForm(request.POST)
       if form.is_valid():
           course_name = form.cleaned_data['course_name']
           tag = form.cleaned_data['tag']
           description = form.cleaned_data['description']
           qualification = form.cleaned_data['qualification']
           times = form.cleaned_data['times']
           price = form.cleaned_data['price']
           info = {'course_name':course_name, 'tag':tag, 'description':description, 'qualification':qualification, 'times':times, 'price':price}
           requests.post('http://exp-api:8000/v1/', info)
    else:
       form = ListingForm()
    return render(request, 'listing.html', {'form': form})


def logout(request):
    #delete cookie and authenticator
    # auth = request.COOKIES.get('auth')
    # if not auth:
    #     # handle user not logged in while trying to create a listing
    #     return HttpResponseRedirect(reverse("login"))
    # resp = delete_cookie_exp()
    # if resp:
    #     return render('home.html', {'success': 'You have been logged out.'})
    # return HttpResponseRedirect(reverse("login"))
    return render(request, 'logout.html')
