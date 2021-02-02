from django.db import models

from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	headline = models.CharField(max_length=300, null=True)
	sub_headline = models.CharField(max_length=500, null=True)
	picture = models.ImageField(null=True, upload_to='images', default='default.png')
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	body = RichTextUploadingField(null=True, blank=True)
	
	def __str__(self):
		return self.headline

	@property
	def get_image(self):
		url = ''
		try:
			url = self.picture.url
		except:
			url = ''
		return url

class Profile(models.Model):
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="default.png")
	bio = models.TextField(null=True, blank=True)
	twitter = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		name = self.first_name
		if self.last_name:
			name += " " + self.last_name
		return name

	@property
	def get_image(self):
		url = ''
		try:
			url = self.profile_pic.url
		except:
			url = ''
		return url

class PostComment(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.body

	
