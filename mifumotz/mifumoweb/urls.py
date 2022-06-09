from django.conf import settings
from django.urls import path
from .views import IndexPage, AboutPage,FaqPage, TeamPage, ContactUs,ArticleDetails,ServicesDetail
urlpatterns = [
    path('',IndexPage.as_view(), name='indexpage'),
    path('About/',AboutPage.as_view(), name='aboutpage'),
    path('FAQ/',FaqPage.as_view(), name='faqpage'),
    path('Team/',TeamPage.as_view(), name='teampage'),
    path('<slug:slug>', ServicesDetail.as_view(), name='service_detail'),
    path('Contactus/',ContactUs.as_view(), name='contactus'),
    path('<slug:slug>', ArticleDetails.as_view(), name='article_detail'),
    path('<slug:slug>', ServicesDetail.as_view(), name='service_detail')
  
    
    
    

    

    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)