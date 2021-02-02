from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .filters import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
			print(user.username)
			user = form.save(commit=False)
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

	page = request.GET.get('page')
	paginator = Paginator(posts, 3)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}

	return render(request, 'posts.html', context)

def postDetail(request, post_name):
	post = Post.objects.get(headline=post_name)

	if request.method == 'POST':
		text = request.POST.get('comment')
		user = request.user.profile
		PostComment.objects.create(
			author = user,
			post = post,
			body = text,
			)

	context = {'post':post}

	return render(request, 'post_detail.html', context)

def createPost(request):
	if request.method == 'POST':
		form = postForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('posts')
		else:
			messages.error(request,'The form is not valid')
	else:
		form = postForm()

	context = {'form':form}

	return render(request, 'create_post.html', context)

def editPost(request, post_name):
	post = Post.objects.get(headline=post_name)
	if request.method == 'POST':
		form = postForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
			return redirect('posts')
		else:
			messages.error(request, 'The form is not valid')
	else:
		form = postForm(instance=post)

	context = {'form':form}

	return render(request, 'create_post.html', context)

def profile(request, user_name):
	user = request.user.profile
	form = profileForm(instance=user)
	if request.method == 'POST':
		form = profileForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile updated!")
			return redirect('profile', request.user.email)

	context = {'user':user, 'form':form}

	return render(request, 'profile.html', context)



