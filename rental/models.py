from django.db import models
from mainapp.models import AppUser
#from django.contrib.auth.models import User



# Create your models here.

class Image(models.Model):
	title = models.CharField(max_length=15)
	image = models.ImageField(upload_to="images/", default="")
	description = models.CharField(max_length=25)
	
	def __str__(self):
		return self.title
		
		
class Landmark(models.Model):
	name = models.CharField(max_length=20)
	walk_time = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name
		
class Apartment(models.Model):
	access_road_condi_choice = (
									("paved", "paved"),
									("unpaved", "unpaved"),
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

	#all default shit
	name = models.CharField(max_length=25, default="none")
	address = models.CharField(max_length=25, default="none")
	university = models.CharField(max_length=25, default="none") #in Nigeria
	price = models.CharField(max_length=10, default="none")
	#description = models.CharField(max_length=25, default="none")
	apartment_type = models.CharField(max_length=30, choices=apartment_type_choice,  default="self contain")
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)# changed to poster's details#########
	poster_phone = models.CharField(max_length=25, default="none")
	poster_name = models.CharField(max_length=25, default="none")
	#photo = ##########################################

	#images = models.ManyToManyField(Image, through="ApartmentImageConnector", through_fields=("apartment", "image"),)
	image1 = models.FileField(upload_to="images/rental")
	image2 = models.FileField(upload_to="images/rental")
	image3 = models.FileField(upload_to="images/rental")
	image4 = models.FileField(upload_to="images/rental")
	image5 = models.FileField(upload_to="images/rental")
	
	landmarks = models.CharField(max_length=125, default="none")
	
	#landmarks = models.ManyToManyField(Landmark, through="ApartmentLandmarkConnector", through_fields=("apartment", "landmark"),)
	
	motorcycle_fare = models.CharField(max_length=20,  default="none")
	vehicle_fare =  models.CharField(max_length=20,  default="none")
	access_road_condi = models.CharField(max_length=10, choices=access_road_condi_choice,  default="paved")
	
	#check box model shit   i njust turned this whole shit to just one extras model
	extras = models.CharField(max_length=100, default="none")
	water = models.CharField(max_length=50,  default="none")
	security = models.CharField(max_length=50,  default="none")
	electricity = models.CharField(max_length=50,  default="none")
	kitchen = models.CharField(max_length=50,  default="none")
	avail_toilet = models.CharField(max_length=50,  default="none")
	bathroom = models.CharField(max_length=50,  default="none")
	avail_tiles = models.CharField(max_length=50,  default="none")
	running_water = models.CharField(max_length=50,  default="none")
	water_storage = models.CharField(max_length=50,  default="none")
	ceiling = models.CharField(max_length=50,  default="none")
	prepared_meter = models.CharField(max_length=50,  default="none")
	lodge_transformer = models.CharField(max_length=50,  default="none")
	
	pub_date = models.DateTimeField("date published")
	
	
	def __str__(self):
		return self.name
		
		
class ApartmentImageConnector(models.Model):
	image = models.ForeignKey(Image, on_delete=models.CASCADE, default="")
	apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, default="")

	reg_id = models.CharField(max_length=60)
	reg_date = models.DateField(auto_now=True)
	
class ApartmentLandmarkConnector(models.Model):
	landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, default="")
	apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, default="")

	reg_id = models.CharField(max_length=60)
	reg_date = models.DateField(auto_now=True)

