# Create your views here.
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'basesite/home.html'

class About(TemplateView):
    template_name = 'basesite/about.html'

class Contact(TemplateView):
    template_name = 'basesite/sitecontact.html'

