from multiprocessing import context
from django.shortcuts import render,redirect
from .models import post
from .forms import NewPostForm

def home_view(request):
    post_list=post.objects.all().order_by('-published_date')
    context={'post_list':post_list,}
    return render(request,'blog/home.html',context)

def detail_view(request, slug):
    posts=post.objects.get(slug=slug)
    context={
        'post':posts,
    }
    return render(request,'blog/post_detail.html',context)

def post_view(request):
    form=NewPostForm()
    if request.method == 'POST':
        form=NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form' : form,
    }


    return render(request,'blog/new_post.html',context)