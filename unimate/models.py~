from django.db import models
from mainapp.models import AppUser
from django.contrib.auth.models import User



# Create your models here.
class Hobby(models.Model):
	name = models.CharField(max_length=50,  default="none")
	
	def __str__(self):
		return self.name
		
		
class RoomMate(models.Model):

	religion_choice = (
			("christian", "christian"),
			("muslim", "muslim"),
			("none", "none"),
	)
	
	apartment_type_choice = (
									("hostel", "hostel"),
									("self contain", "self contain"),
									("single room self contain", "single room self contain"),
									("two rooms self contain", "two rooms self contain"),
									("one bedroom flat", "one bedroom flat"),
									("two bedroom flat", "two bedroom flat"),
									("three bedroom flat", "three bedroom flat"),

	)
	#personal details
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE) #changed to poster's details#########
	
	#room mate details
	#university = models.ForeignKey(University, on_delete=models.CASCADE, default="")
	#age = models.CharField(max_length=50,  default="none")
	religion = models.CharField(max_length=10, choices=religion_choice,  default="none")
	department = models.CharField(max_length=50,  default="none")
	university = models.CharField(max_length=25, default="none")
	hobbies = models.CharField(max_length=25, default="none")
	host_name = models.CharField(max_length=25, default="none")
	host_phone = models.CharField(max_length=25, default="none")
	#state = foreign
	language = models.CharField(max_length=50,  default="none")
	
	#apartment details
	apartment_name = models.CharField(max_length=50,  default="none")
	apartment_type = models.CharField(max_length=30, choices=apartment_type_choice,  default="self contain")
	address = models.CharField(max_length=50,  default="none")
	description = models.CharField(max_length=50,  default="none")
	landmarks = models.CharField(max_length=50,  default="none")
	
	photo = models.ImageField(upload_to="images/", default="")
	
	duration_1 = models.CharField(max_length=50,  default="none")
	duration_2 = models.CharField(max_length=50,  default="none")
	unimate_no = models.CharField(max_length=5,  default="none")
	
	image1 = models.FileField(upload_to="images/unimate")
	image2 = models.FileField(upload_to="images/unimate")
	image3 = models.FileField(upload_to="images/unimate")
	
	extras = models.CharField(max_length=100, default="none")
	
	pub_date = models.DateTimeField("date published")
	
	def __str__(self):
		return self.apartment_name


class RoomMateHobbyConnector(models.Model):
	room_mate = models.ForeignKey(RoomMate, on_delete=models.CASCADE, default="")
	hobby= models.ForeignKey(Hobby, on_delete=models.CASCADE, default="")

	reg_id = models.CharField(max_length=60)
	reg_date = models.DateField(auto_now=True)

