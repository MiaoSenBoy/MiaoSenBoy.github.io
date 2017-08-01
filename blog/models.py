#coding=utf-8
from django.db import models

# Create your models here.

class MyblogModel(models.Model):
    blog_title = models.CharField(max_length=20)  # 博客标题
    blog_text = models.TextField() #博客内容
    blog_date = models.DateTimeField(auto_now_add=True)  # 发布日期
    blog_bread = models.IntegerField(default=0)  # 阅读量
    blog_comment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除
