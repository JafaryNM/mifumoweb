from re import T
from django.urls import path
from .views import IndexPage, AboutPage,FaqPage, TeamPage, ContactUs

urlpatterns = [
    path('',IndexPage.as_view(), name='indexpage'),
    path('About/',AboutPage.as_view(), name='aboutpage'),
    path('FAQ/',FaqPage.as_view(), name='faqpage'),
    path('Team/',TeamPage.as_view(), name='teampage'),
    path('Contactus/',ContactUs.as_view(), name='contactus')
    
]
