from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import BlogPostForm
from .models import BlogPost
# Create your views here.
def display_blogposts(request):
    blog_posts = BlogPost.objects.all()

    blog_posts = reversed(blog_posts) # so the most recent blogpost would be up top
    return render(request, 'blog.html', {'blog_posts': blog_posts})
    # return HttpResponse("HELLO WORKING BLOGGGGGG")

def single_blogpost(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)

    return render(request, 'single_blogpost.html', {'blogpost': blogpost})

@login_required
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST) # pass POST data to the form
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
            return redirect('display_blogposts') #redirect to the view with all of the blogposts
    else:
        form = BlogPostForm()  # Assign empty form for GET requests

    return render(request, 'blog_post_form.html', {'form': form})
