from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class signupForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'password1', 'password2' , 'email')

class postForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}