from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogPost
# Create your views here.
def display_blogposts(request):
    blog_posts = BlogPost.objects.all()

    return render(request, 'blog.html', {'blog_posts': blog_posts})
    # return HttpResponse("HELLO WORKING BLOGGGGGG")