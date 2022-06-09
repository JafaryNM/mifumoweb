from calendar import c
from typing import List
from django.shortcuts import render
from .models import Article, Service
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class IndexPage(ListView):
    
    template_name='index.html'
    model=Article
    model=Service
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['articles']=Article.objects.all()
        context['services']=Service.objects.all()
        return context
    
class ArticleDetails(DetailView):
    model=Article
    template_name='article_detail.html'
    
    
class ServicesDetail(DetailView):
    model=Service
    template_name='service_details.html'
    
    
    
class AboutPage(TemplateView):
    
    template_name='about.html'
    
class FaqPage(TemplateView):
    
    template_name='faq.html'
    
class TeamPage(TemplateView):
    
    template_name='team.html'
    
class ContactUs(TemplateView):
    
    template_name='contact.html '
    



    
    
    
    
    