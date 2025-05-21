from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import BlogPostForm
from .models import BlogPost
# Create your views here.
def display_blogposts(request):
    blog_posts = BlogPost.objects.all()

    return render(request, 'blog.html', {'blog_posts': blog_posts})
    # return HttpResponse("HELLO WORKING BLOGGGGGG")

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST) # pass POST data to the form
        if form.is_valid():
            form.save() #save the blgopost to the databse
            return redirect('display_blogposts') #redirect to the view with all of the blogposts
    else:
        form = BlogPostForm()  # Assign empty form for GET requests

    return render(request, 'blog_post_form.html', {'form': form})
