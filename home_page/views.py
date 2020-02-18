from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'home_page/index.html'

class AboutView(generic.TemplateView):
    template_name = 'home_page/about.html'