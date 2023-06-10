from django.shortcuts import render,redirect
from django.http import HttpResponse
from Blogger.models import Post,BloggerComment
from django.contrib import messages
from Blogger.templatetags import extras

# Create your views here.

def BlogHome(request):
    allPost = Post.objects.all()
    context = {'allPost':allPost}
    return render(request, 'Blogger/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BloggerComment.objects.filter(post=post, parent=None)
    replies = BloggerComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.Sno not in replyDict.keys():
            replyDict[reply.parent.Sno] = [reply]
        else:
            replyDict[reply.parent.Sno].append(reply)
    context = {'post':post, 'comments':comments, 'replyDict':replyDict}
    return render(request, 'Blogger/blogPost.html', context)

def blogComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(Sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BloggerComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, 'Your Comment has been Successfully posted')
        else :
            parent = BloggerComment.objects.get(Sno=parentSno)
            comment = BloggerComment(comment=comment, user=user, post=post, parent=parent)
        
            comment.save()
            messages.success(request, 'Your Reply has been Successfully posted')
    return redirect(f"/blog/{post.slug}")