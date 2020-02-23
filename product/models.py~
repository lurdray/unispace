from django.db import models
from mainapp.models import AppUser
# Create your models here.

class Product(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=15, default="none")
	description = models.CharField(max_length=50, default="none")
	price = models.CharField(max_length=15, default="none")
	university = models.CharField(max_length=25, default="none")
	
	image1 = models.FileField(upload_to="images/product")
	image2 = models.FileField(upload_to="images/product")
	image3 = models.FileField(upload_to="images/product")
	
	tags = models.CharField(max_length=125, default="none")
	
	pub_date = models.DateTimeField("date published")
	
	def __str__(self):
		return self.name
