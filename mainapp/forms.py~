from django.contrib.auth.models import User
from django import forms
from mainapp.models import AppUser, Extras
from rental.models import Apartment
from unimate.models import RoomMate
from product.models import Product
#from unimate.models import 


class PostRentalForm(forms.ModelForm):
	subjects = Extras.objects.all()
	subject_listk = []
	extras_list = []
	try:
		for subject in subjects:
			subject_listk.append(subject)
			subject_listk.append(subject)
			subject_listk = tuple(subject_listk)
			subject_list.append(subject_listk)
			subject_listk = []
		extras_list = tuple(extras_list)

	except:
		pass
		
	extras = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=extras_list,)

	class Meta():
		model = Apartment
		fields = ("name",  "address", "price", "university", "apartment_type",  "extras", "landmarks", "image1", "image2", "image3", "image4", "image5")
		
		
		
class PostRoomMateForm(forms.ModelForm):
	
	class Meta():
		model = RoomMate
		fields = ("apartment_name", "address", "description")

class PostProductForm(forms.ModelForm):
	
	class Meta():
		model = Product
		fields = ("name", "price", "description", "image1", "image2", "image3", "university")


class UserForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ("username", "password1", "password2", "email" )
		

class ResultForm(forms.Form):
	search = forms.CharField( max_length=25)
	search_category = forms.CharField(max_length=25)
		
class ProfileForm(forms.Form):
	profle_name = forms.CharField( max_length=25)
	profile_phone = forms.CharField( max_length=25)
	profile_university = forms.CharField( max_length=25)
	profile_hobbies = forms.CharField( max_length=25)
	profile_languages = forms.CharField( max_length=25)
	profile_department = forms.CharField( max_length=25)
	profile_phone = forms.CharField(widget=forms.FileInput())
	
		

class SignUpForm(forms.ModelForm):

	class Meta():
		model = AppUser
		fields = ("name", )
		
		
class LoginForm(forms.Form):
	username = forms.CharField(label="username", max_length=25)
	password = forms.CharField(label="password", widget=forms.PasswordInput())

	
