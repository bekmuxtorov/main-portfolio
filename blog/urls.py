from django.urls import path
from .models import Blog
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name = "blog"), 
    path('/<int:pk>/',BlogDetailView.as_view(), name = 'blog_detail' ),
]

