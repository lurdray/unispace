from django.urls import path
from django.conf.urls import url
from . import views

app_name = "mainapp"

urlpatterns = [
	path("", views.IndexView, name="index"),
	path("signup/", views.SignUpView, name="signup"),
	path("login/", views.LoginView, name="login"),
	
	path("main/", views.MainView, name="main"),
	path("profile/", views.ProfileView, name="profile"),
	path("postrental/", views.PostRentalView, name="postrental"),
	#path("detail/", views.RentalDetailView, name="rental_detail"),
	url(r"^rental/(?P<rental_id>[0-9]+)/$", views.RentalDetailView, name="rental_detail"),
	
	path("postroommate/", views.PostRoomMateView, name="postroommate"),
	url(r"^unimate/(?P<unimate_id>[0-9]+)/$", views.UnimateDetailView, name="unimate_detail"),
	
	path("postproduct/", views.PostProductView, name="postproduct"),
	url(r"^product/(?P<product_id>[0-9]+)/$", views.ProductDetailView, name="product_detail"),
	
	path("allpost/", views.AllPostView, name="all_post"),
	
	path("about/", views.AboutView, name="about"),
	path("termsandcondition/", views.TacView, name="tac"),
	
	
	
	
	path("userlogout/", views.UserLogoutView, name="userlogout"),

	

]
