from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog

# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
