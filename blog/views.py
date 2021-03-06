from ast import keyword
import imp
from django.db import reset_queries
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.conf import settings
from .form import Blogform
import os
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    pagnum = request.GET.get('page')
    blogs = paginator.get_page(pagnum)
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Blogform()
        return render(request, 'new.html', {'form':form})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk = id)
    
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            edit_blog.title = form.cleaned_data['title']
            edit_blog.content = form.cleaned_data['content']
            edit_blog.image = form.cleaned_data['image']
            edit_blog.save()
            return redirect('detail', edit_blog.id)
    else:
        form = Blogform(instance= edit_blog)
        return render(request, 'edit.html', {'form':form})

"""
def update(request, id):
    update_blog = get_object_or_404(Blog, pk = id)
    update_blog.title = request.POST['title']
    update_blog.content = request.POST['content']
    update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('detail', update_blog.id)
"""
def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk = id)
    delete_blog.delete()
    return redirect('home')

#?????? ?????? ??????
def search(request):
    search_blog = Blog.objects.all() #?????? ????????????
    
    if 'keyword' in request.GET: #????????? ???????????? GET????????? ?????????
        keyword = request.GET['keyword'] #keyword ????????? ????????? ????????? ??????
        if keyword: #keyword??? ???????????? 
            search_blog = search_blog.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
            #search_blog ????????? title, content??? ?????? ???????????? ?????? ????????? ??????
    context = {
        'search_blog' : search_blog, #?????? ??? ??????
        }
    return render(request, 'search.html', context) #?????? ??? ??????