#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from django.core.paginator import Paginator, Page
# Create your views here.

#博客首页
def index(request):
    # myblog1 =
    blog_list =MyblogModel.objects.order_by('-blog_date')
    # paginator = Paginator(blog_list)
    # # if
    # page = paginator(page)
    # print(blog_list)
    content = {'title':'MiaoSen博客-首页','blog_list':blog_list}
    return render(request, 'blog/index.html', content)

#关于
def about(request):
    content = {'title':'MiaoSen博客-关于'}
    return render(request, 'blog/about.html', content)

#博客样式
def post(request):
    content = {'title':'MiaoSen博客-博客样式'}
    return render(request, 'blog/post.html', content)

#个人信息
def contact(request):
    content = {'title':'MiaoSen博客-作者信息'}
    return render(request, 'blog/contact.html', content)

def write_blog(request):
    content = {'title':'MiaoSen博客-写博客'}
    return render(request, 'blog/write_blog.html', content)

def get_blog(request):
    myblog = MyblogModel()
    #获取博客标题
    blog_titles = request.POST.get('blog_biaoti')
    #获取博客内容
    blog_text = request.POST.get('blog_text')
    myblog.blog_title = blog_titles
    myblog.blog_text = blog_text
    myblog.save()
    return redirect('/index/')


