from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post # Postモデルをimport

class PostListView(generic.ListView):
    model = Post # 一覧表示させたいモデルを呼び出し

class PostCreateView(generic.CreateView): # 追加
    model = Post # 作成したい model を指定
    form_class = PostCreateForm # 作成した form クラスを指定
    success_url = reverse_lazy('blog:post_list') # 記事作成に成功した時のリダイレクト先を指定

class PostDetailView(generic.DetailView): 
    model = Post # pk(primary key)はurls.pyでしているのでここではmodelを呼び出すだけ

class PostUpdateView(generic.UpdateView):
    model = Post 
    form_class = PostCreateForm # PostCreateFormはそのまま活用できる
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(generic.DeleteView):
    model = Post 
    success_url = reverse_lazy('blog:post_list')