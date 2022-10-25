from django.shortcuts import render
from django.views.generic import TemplateView, View

# define the home view
class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")
    
    def post(self, request):
        pass