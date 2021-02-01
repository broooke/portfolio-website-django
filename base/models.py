from django.db import models


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
	
