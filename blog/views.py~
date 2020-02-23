from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def BlogDetailView(request, blog_id):
	#return HttpResponse(blog_id)
	blog = Blog.objects.get(pk=blog_id)
	context = {"blog": blog}
	return render(request, "mainapp/blog.html", context)
	
