from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexPage(TemplateView):
    
    template_name='index.html'

class AboutPage(TemplateView):
    
    template_name='about.html'
    
class FaqPage(TemplateView):
    
    template_name='faq.html'
    
class TeamPage(TemplateView):
    
    template_name='team.html'
    
class ContactUs(TemplateView):
    
    template_name='contact.html '
    
    
    
    
    
    
    
    