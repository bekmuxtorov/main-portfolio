from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Works

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html' 

class WorksListView(ListView):
    model = Works
    template_name = 'works.html'