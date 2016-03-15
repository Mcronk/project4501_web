from django import forms

class SignupForm(forms.Form):
	user_name = forms.CharField(label='User name', max_length=20)
	password = forms.CharField(label='Password', max_length=20)
	email = forms.CharField(label='Email', max_length=20)
	phone = forms.CharField(label='Phone', max_length=20)
	#This should be charfield too in models
class LoginForm(forms.Form):
	user_name = forms.CharField(label='User name', max_length=20)
	password = forms.CharField(label='Password', max_length=20)
	
class ListingForm(forms.Form):
	course_name = forms.CharField(label='Course Name', max_length=20)
	tag = forms.CharField(label='Tag', max_length=20)
	description = forms.CharField(label='Description', max_length = 50)
	qualification = forms.CharField(label='Qualifications', max_length=30)
	times = forms.CharField(label='Available Times', max_length=50)
	price = forms.IntegerField(label='Price per Hour')
	#tutor
