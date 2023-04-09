from django.shortcuts import render
from django.views import generic
from .models import Post # Postモデルをimport

class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'

class PostListView(generic.ListView):
    model = Post # 一覧表示させたいモデルを呼び出し


# Create your views here.
