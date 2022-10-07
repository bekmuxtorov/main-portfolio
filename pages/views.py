from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .const import Const
from .models import Works,Home

# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'home.html' 

def HomePageView(request):
    object = list(Home.objects.all().order_by('-date'))[0]
    return render(request, 'home.html', {'object':object})

class WorksListView(ListView):
    model = Works
    template_name = 'works.html'

    def get_context_data(self, **kwargs):
        context = super(WorksListView, self).get_context_data(**kwargs)
        context["project_directions"] = dict(Const.project_directions)
        return context

class WorkDetailView(DetailView):
    model = Works
    template_name = 'works_detail.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
     
