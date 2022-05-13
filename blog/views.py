from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import(
    CreateView,
    DeleteView,
    UpdateView,
)


class BlogListView(ListView):
    template_name = "home.html"
    model = Post

class BlogCreateView(CreateView):
    template_name = "post_new.html"
    model = Post
    fields = ['title', 'author', 'body']

class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

class BlogUpdateView(UpdateView):
    template_name = "post_edit.html"
    model = Post
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    template_name = "post_delete.html"
    model = Post
    success_url = reverse_lazy('home')
    
