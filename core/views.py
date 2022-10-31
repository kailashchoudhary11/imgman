from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.core import mail
from django.conf import settings

# define the home view
class HomeView(TemplateView):
    '''
    Sets the home page.
    '''
    template_name = 'index.html'

class AboutView(TemplateView):
    '''
    Sets the about page.
    '''
    template_name = 'about.html'

class ContactView(View):
    '''
    Sets the contact page.
    '''
    def get(self, request):
        return render(request, "contact.html")
    
    def post(self, request):
        name = request.POST.get("name")
        email_id = request.POST.get("email")
        msg = request.POST.get("message")

        # Manually open the connection
        connection = mail.get_connection()
        connection.open()
        body = f'''Name: {name}\n
Email: {email_id}\n
Message: {msg}\n
        '''
        # Construct an email message that uses the connection
        email = mail.EmailMessage(
            'Imgman Contact Form',
            body,
            settings.EMAIL_HOST_USER,
            ['kaijat108@gmail.com'],
            connection=connection,
        )
        email.send() # Send the email
        return redirect(reverse_lazy("core:index"))