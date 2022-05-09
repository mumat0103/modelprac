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


def update(request, id):
    update_blog = get_object_or_404(Blog, pk = id)
    update_blog.title = request.POST['title']
    update_blog.content = request.POST['content']
    update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk = id)
    delete_blog.delete()
    return redirect('home')

#검색 기능 추가
def search(request):
    search_blog = Blog.objects.all() #객체 가져오기
    
    if 'keyword' in request.GET: #입력한 키워드가 GET요청에 있으면
        keyword = request.GET['keyword'] #keyword 변수에 입력한 키워드 저장
        if keyword: #keyword가 존재하면 
            search_blog = search_blog.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
            #search_blog 변수의 title, content에 해당 키워드가 있는 객체를 할당
    context = {
        'search_blog' : search_blog, #찾은 값 저장
        }
    return render(request, 'search.html', context) #찾은 값 반환