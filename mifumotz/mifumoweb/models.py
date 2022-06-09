from datetime import date
from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse



# Create your models here.

class Service(models.Model):
    
    title = models.CharField(max_length = 150, null=False)
    slug = models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to='images/', null=True)
    descritption = models.TextField(max_length=300, null=True)
    created_at = models.DateField(auto_now=True)
    
    
    
    def __str__(self):
        
        return self.title 
    
    
    def get_absolute_url(self):
        
        return reverse("service_detail", kwargs={"slug":self.slug})
    
    
    
        
     
    
class Article(models.Model):
    
    title = models.CharField(max_length = 150, null=True)
    slug = models.SlugField(max_length = 50, null=True)
    description = models.TextField()
    date = models.DateField(auto_now=True,)
    image = models.ImageField(upload_to='images/', null=True)

    
    
    def __st__(self):
        
        return self.title
    
    def get_absolute_url(self):
        
        
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    
    
    
