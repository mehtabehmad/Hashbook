from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect

from .models import Post, Comment


# Create your views here.

def index(request):

    return render(request, 'HashbookApp/index.html')


def posts(request):
    posts = Post.objects.order_by('-date_published')    
    comments = Comment

    context = {"posts":posts, 'comments':comments}
    return render(request, 'HashbookApp/posts.html', context)

@login_required()
def post(request, post_id):
    post = Post.objects.get(pk = post_id)
    comments = Comment.objects.order_by('-date_published').filter(post=post_id)
    
    context = {"post":post,"comments": comments}
    return render(request, 'HashbookApp/post.html', context)

@login_required()
def newpost(request):
    if request.method == 'POST':

        new_post = Post()
        new_post.title = request.POST['title']
        new_post.text = request.POST['text']

        new_post.author = request.user
        new_post.save()

        return HttpResponseRedirect(reverse('HashbookApp:posts'))
        

    else:
        return render(request, 'HashbookApp/newpost.html')

    

@login_required()
def comment(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == 'POST':

        new_comment = Comment()
        new_comment.text = request.POST['text']

        new_comment.post = post
        new_comment.author = request.user
        new_comment.save()

        return HttpResponseRedirect(reverse('HashbookApp:post', args=[post.id]))
        

    else:
        return render(request, 'HashbookApp/comment.html', {'post':post})


@login_required()
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    
    return HttpResponseRedirect(reverse('HashbookApp:posts'))

@login_required()
def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':

        post_edit = post
        post_edit.title = request.POST['title']
        post_edit.text = request.POST['text']

        post_edit.author = request.user
        post_edit.save()

        return HttpResponseRedirect(reverse('HashbookApp:post', args=[post.id]))

    else:
        return render(request, 'HashbookApp/edit.html', {'post':post})
    
@login_required()
def cdelete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return HttpResponseRedirect(reverse('HashbookApp:post', args=[comment.post.id]))

@login_required()
def cedit(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post = comment.post

    if request.method == 'POST':

        comment_edit = comment
        comment_edit.text = request.POST['text']

        comment_edit.author = request.user
        comment_edit.save()

        return HttpResponseRedirect(reverse('HashbookApp:post', args=[comment.post.id]))

    else:
        return render(request, 'HashbookApp/cedit.html', {'comment':comment, 'post':post})