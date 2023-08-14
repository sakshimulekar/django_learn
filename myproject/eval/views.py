from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(view_posts)
        else:
            form = PostForm()
        return render(request,'create_post.html',{'form':form})
    

def view_posts(request):
    posts = Post.objects.all()
    return render(request,'view_posts.html',{'posts':posts})

def delete_post(request,post_id):
    post = get_object_or_404(Post,pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('view_posts')
    return render(request,'delete_post',{'post':post})
# Create your views here.
