from django.db import models
from mainapp.models import AppUser

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=20, default="")
	content_brief = models.CharField(max_length=50, default="")
	content_main = models.CharField(max_length=250, default="")
	tags = models.CharField(max_length=50, default="")
	pub_date = models.DateTimeField('date published')
	image = models.FileField(upload_to="images/blog")
	#author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
