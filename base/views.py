from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .filters import *
from .models import *

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login

# Create your views here.

def home(request):
	return render(request,'home.html')

def send_email(request):
	if request.method == 'POST':
		template = render_to_string('email_dict.html', {
			'name': request.POST['name'],
			'email': request.POST['email'],
			'message': request.POST['message'],
			})

		email = EmailMessage(
				request.POST['subject'],
				template,
				settings.EMAIL_HOST_USER,
				[request.POST['email']]
			)

		email.fail_silently = False 
		email.send()

	return render(request,'email_send.html')

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, "User with this email does not exists")

		if user is not None:
			dj_login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')
				
	return render(request,'login.html')

def signup(request):
	if request.method == 'POST':
		form = signupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.first_name + " " + user.last_name
			user.save()
			messages.success(request, 'Account successfully created!')

			user = authenticate(username=user.username, password=request.POST['password1'])
			if user is not None:
				dj_login(request, user)
				return redirect('home')
		else:
			messages.error(request, 'The form is not valid')
	else:
		form = signupForm()

	context = {'form':form}

	return render(request, 'register.html', context)

def logOut(request):
	logout(request)
	return redirect('login')

def posts(request):
	posts = Post.objects.all()
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'posts.html', context)

