from django import contrib
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from blog.models import Post, BlogComment
from django.contrib import messages
import random

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all().order_by('-timeStamp')
    # print(allPosts)
    context = {'allPosts': allPosts}
    return render(request, 'blog/blog.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post).order_by('-timestamp')

    allPosts = Post.objects.all()[0:3]
    # print(allPosts)
    context = {
        'post': post,
        'allPosts' : allPosts,
        'comments' : comments
        }

    return render(request, 'blog/blogpost.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('commentContent')
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)

        if comment == "":
            messages.error(request, "You cannot post a blank comment")
            return redirect(f"/blog/{post.slug}")

        elif len(comment) > 2000:
            messages.error(request, "Your Comment is too long !")
            return redirect(f"/blog/{post.slug}")
        else:
            user=request.user

            comment=BlogComment(comment= comment, user=user, post=post)
                
                
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")


