from django.shortcuts import render
from django.views.generic import TemplateView

# define the home view
class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'