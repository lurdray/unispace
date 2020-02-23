from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class University(models.Model):
	name = models.CharField(max_length=55)
	abbr = models.CharField(max_length=15, default="none")
	state = models.CharField(max_length=25)
	
	def __str__(self):
		return self.name
		
class Extras(models.Model):
	name = models.CharField(max_length=25)
	
	def __str__(self):
		return self.name


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	age = models.CharField(max_length=25)
	religion = models.CharField(max_length=25)
	phone = models.CharField(max_length=25)
	department = models.CharField(max_length=25)
	university = models.CharField(max_length=25, default="none")
	language = models.CharField(max_length=25, default="none")
	hobbies = models.CharField(max_length=25, default="none")
	#university = models.ForeignKey(University, on_delete=models.CASCADE, default="")
	
	schoolidcard_image = models.ImageField(upload_to="images/appuser", default="")
	voterscard_image = models.ImageField(upload_to="images/appuser", default="")
	nationalidcard_image = models.ImageField(upload_to="images/appuser", default="")
	driverslicence_image = models.ImageField(upload_to="images/appuser", default="")
	
	photo = models.ImageField(upload_to="images/appuser", default="")

	def __str__(self):
		return self.name
	
