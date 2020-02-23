from django.shortcuts import render, get_object_or_404
from .forms import UserForm, SignUpForm, LoginForm, PostRentalForm, PostRoomMateForm, ResultForm, ProfileForm, PostProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils import timezone

from .models import AppUser, University, Extras
from rental.models import Apartment
from unimate.models import RoomMate
from product.models import Product
from blog.models import Blog


# Create your views here.

def PostProductView(request):
	if request.method == "POST":
		form = PostProductForm(request.POST or None, request.FILES or None)
		app_user = get_object_or_404(AppUser, user__pk=request.user.id)
		
		product = Product.objects.create(app_user=app_user, name=request.POST.get("name"), price=request.POST.get("price"), description=request.POST.get("description"), university=request.POST.get("university"),image1=request.FILES["image1"],image2=request.FILES["image2"],image3=request.FILES["image3"], tags=request.POST.get("tags"),pub_date=timezone.now())
		
		product.save()
		return HttpResponseRedirect(reverse("mainapp:main"))
		
	else:
		form = PostProductForm()
		universities = University.objects.all()
		context = {"form": form, "universities": universities}
		return render(request, "mainapp/post_product.html", context)

def PostRentalView(request):

	if request.method == "POST":
		
		#if 
		
		form = PostRentalForm(request.POST or None, request.FILES or None)
		app_user = get_object_or_404(AppUser, user__pk=request.user.id)

		apartment = Apartment.objects.create(app_user=app_user, name=request.POST.get("name"),address=request.POST.get("address"),university=request.POST.get("university"),price=request.POST.get("price"),apartment_type=request.POST.get("apartment_type"),poster_name=app_user.name,poster_phone=app_user.phone,landmarks=request.POST.get("landmarks"),extras=request.POST.getlist("extras"), image1=request.FILES["image1"], image2=request.FILES["image2"], image3=request.FILES["image3"], image4=request.FILES["image4"], image5=request.FILES["image5"], pub_date=timezone.now())
		
		apartment.save()

		return HttpResponseRedirect(reverse("mainapp:main"))
	
	else:
		form = PostRentalForm()
		universities = University.objects.all()
		extras = Extras.objects.all()
		context = {"form": form, "universities": universities, "extras": extras}
		return render(request, "mainapp/post_rental.html", context)
		
		
def ProductDetailView(request, product_id):
	result = Product.objects.get(pk=product_id)
	context = {"result": result}
	return render(request, "mainapp/result_product_detail.html", context)


def RentalDetailView(request, rental_id):
	result = Apartment.objects.get(pk=rental_id)
	context = {"result": result}
	return render(request, "mainapp/result_rental_detail.html", context)
	
def UnimateDetailView(request, unimate_id):
	result = RoomMate.objects.get(pk=unimate_id)
	context = {"result": result}
	return render(request, "mainapp/result_unimate_detail.html", context)
	
def PostRoomMateView(request):
	app_user = get_object_or_404(AppUser, user__pk=request.user.id)
	if request.method == "POST":
		form = PostRoomMateForm(request.POST or None, request.FILES or None)
		
		
		roommate = RoomMate.objects.create(app_user=app_user,host_name=request.POST.get("host_name"), host_phone=request.POST.get("host_phone"),apartment_name=request.POST.get("apartment_name"),religion=request.POST.get("religion"),apartment_type=request.POST.get("apartment_type"),address=request.POST.get("address"),description=request.POST.get("description"), department=request.POST.get("department"),language=request.POST.get("language"),hobbies=request.POST.get("hobbies"),photo=request.POST.get("host_photo"), university=request.POST.get("university"),image1=request.FILES["image1"], image2=request.FILES["image2"], image3=request.FILES["image3"], extras=request.POST.getlist("extras"), landmarks=request.POST.get("landmarks"),duration_1=request.POST.get("duration_1"),duration_2=request.POST.get("duration_2"),unimate_no=request.POST.get("unimate_no"),pub_date=timezone.now())
		
		roommate.save()
		

		return HttpResponseRedirect(reverse("mainapp:main"))
	
	else:
		form = PostRoomMateForm()
		extras = Extras.objects.all()
		context = {"app_user": app_user, "form": form, "extras": extras}
		return render(request, "mainapp/post_roommate.html", context)
		
		
		
def AboutView(request):
	return render(request, "mainapp/about.html")
	
def TacView(request):
	return render(request, "mainapp/tac.html")


def IndexView(request):
	form = ResultForm(data=request.POST)
	if request.method == "POST":
		apartments = Apartment.objects.order_by("-pub_date")[:6]
		unimates = RoomMate.objects.order_by("-pub_date")[:6]
		products = Product.objects.order_by("-pub_date")[:6]
		search = request.POST.get("search")
		search_category = request.POST.get("search_category")
		result_box = set([])
		#result_box = []
		if search_category == "rental":
			results = Apartment.objects.all()
			search_split = str(search.split(" "))
		
			for result in results:
				for var1, var2 in zip(result.landmarks, search_split):
					if var1 == var2:
						result_box.add(result)
						#result_box.append(result)
					else:
						pass
						
			context = {"results": result_box, "form": form, "apartments": apartments}
			return render(request, "mainapp/result_rental.html", context)
			
		elif search_category == "product":
			results = Product.objects.all()
			search_split = str(search.split(" "))
		
			for result in results:
				for var1, var2 in zip(result.tags, search_split):
					if var1 == var2:
						result_box.add(result)
						#result_box.append(result)
					else:
						pass
						
			context = {"results": result_box, "form": form, "products": products}
			return render(request, "mainapp/result_product.html", context)

		else:
			#search_category == "unimate":
			results = RoomMate.objects.all()
			search_split = str(search.split(" "))
			
			for result in results:
				for var1, var2 in zip(result.landmarks, search_split):
					if var1 == var2:
						result_box.add(result)
						#result_box.append(result)
					else:
						pass
						
			context = {"results": result_box, "form": form, "unimates": unimates}
			return render(request, "mainapp/result_unimate.html", context)

	else:
		apartment = Apartment.objects.order_by("-pub_date")[0]
		unimate = RoomMate.objects.order_by("-pub_date")[0]
		product = Product.objects.order_by("-pub_date")[0]
		context = {"apartment": apartment, "unimate": unimate, "product": product, "form": form}
		#return HttpResponse(apartments)
		return render(request, "mainapp/index.html", context)
	
def ResultView(request):
	if request.method == "POST":
		pass	
	else:
		return HttpResponse("fuck off!!!!")
		
def ProfileView(request):
	form = ProfileForm(request.POST or None, request.FILES or None)
	app_user = AppUser.objects.get(user__pk=request.user.id)
	
	if request.method == "POST":
		app_user = AppUser.objects.filter(user__pk=request.user.id)
		#AppUser.objects.filter(user__pk=request.user.id)
		app_user.update(name=request.POST.get("profile_name"), phone=request.POST.get("profile_phone"), university=request.POST.get("profile_university"), language=request.POST.get("profile_languages"), hobbies=request.POST.get("profile_hobbies"), department=request.POST.get("profile_department"))
		
		# 
		app_user = AppUser.objects.get(user__pk=request.user.id)
		app_user.photo=request.FILES["profile_photo"]
		app_user.driverslicence_image=request.FILES["driverslicence_image"]
		app_user.nationalidcard_image=request.FILES["nationalidcard_image"]
		app_user.voterscard_image=request.FILES["voterscard_image"]
		app_user.schoolidcard_image=request.FILES["schoolidcard_image"]
		app_user.save()

		return HttpResponseRedirect(reverse("mainapp:main"))
	
	else:
		
		#form = ProfileForm(initial={"profile_phone": app_user.name})	
		context = {"app_user": app_user, "form":form}
	
		return render(request, "mainapp/profile.html", context)
	
def MainView(request):
	form = ResultForm(data=request.POST)
	if request.method == "POST":
		apartments = Apartment.objects.all()
		search = request.POST.get("search")
		search_category = request.POST.get("search_category")
		result_box = set([])
		#result_box = []
		if search_category == "rental":
			results = Apartment.objects.all()
			search_split = str(search.split(" "))
		
			for result in results:
				for var1, var2 in zip(result.landmarks, search_split):
					if var1 == var2:
						result_box.add(result)
						#result_box.append(result)
					else:
						pass
						
			context = {"results": result_box, "form": form, "apartments": apartments}
			return render(request, "mainapp/result_rental.html", context)

		else:
			#search_category == "unimate":
			results = RoomMate.objects.all()
			search_split = str(search.split(" "))
			
			for result in results:
				for var1, var2 in zip(result.landmarks, search_split):
					if var1 == var2:
						result_box.add(result)
						#result_box.append(result)
					else:
						pass
						
			context = {"results": result_box, "form": form, "apartments": apartments}
			return render(request, "mainapp/result_unimate.html", context)
			
			
	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)
		apartments = Apartment.objects.filter(app_user=app_user)
		
		apartments = apartments.order_by("-pub_date")[:12]
		apartment_no = apartments.count()
		roommates = RoomMate.objects.filter(app_user=app_user)
		roommate_no = roommates.count()
		blogs = Blog.objects.order_by("-pub_date")[:6]
		
	
		context = {"app_user": app_user, "apartments":apartments, "apartment_no":apartment_no, "roommate_no":roommate_no, "blogs":blogs, "apartments":apartments}
	
		return render(request, "mainapp/main.html", context)
		
	
def UserLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("mainapp:index"))


def LoginView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:

				app_user = AppUser.objects.get(user=user)
				login(request, user)
				messages.add_message(request, messages.INFO, "you're logged in!")
				return HttpResponseRedirect(reverse("mainapp:main"))
			else:
				pass

		else:
			messages.add_message(request, messages.INFO, "invalid login details!")
			return HttpResponseRedirect(reverse("mainapp:login"))

	else:
		form = LoginForm()
		return render(request, "mainapp/login.html", {"form": form})	

def SignUpView(request):
	if request.method == "POST":
		form1 = SignUpForm(request.POST or None, request.FILES or None)
		form2 = UserForm(request.POST or None, request.FILES or None)
		
		if request.POST.get("password2") != request.POST.get("password1"):
			messages.add_message(request, messages.INFO, "Both passwords must be the same")
			return HttpResponseRedirect(reverse("mainapp:signup"))
			#messages.add_message(request, messages.INFO, "Both passwords must be the same")
		#if form1.is_valid() and form2.is_valid():
			#form.save() request.POST.get("password1")
		else:
			user = form2.save()
			user.set_password(request.POST.get("password1"))
			user.save()

			app_user = form1.save(commit=False)
			app_user.user = user
			app_user.photo = request.FILES["photo"]
			app_user.save()

			#else:
			#	return HttpResponse("something went wrong joor!")
				#pass
			return HttpResponseRedirect(reverse("mainapp:login"))
	
	else:
		form1 = SignUpForm()
		form2 = UserForm()
		return render(request, "mainapp/sign_up.html", {"form1": form1, "form2": form2})

	
	
