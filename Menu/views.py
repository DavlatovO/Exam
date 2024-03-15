from django.shortcuts import render
from . import models


def index(request):
    
    about_us = models.AboutUs.objects.last()
    services = models.Service.objects.all()

    prices_list = []

    context = {
        
        'about_us':about_us,
        'services':services,
        'prices':prices_list
    }
    return render(request, 'index.html', context)

def about_us(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }              
    return render(request, 'about.html', context)

def service(request):
    service = models.Service.objects.all()
    context = {
        'service':service
    }              
    return render(request, 'service.html', context)



def contact(request):
    if request.method == 'POST':
            
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
    return render(request, 'contact.html')

def blog(request):
   
   
    blog_posts = models.Blog.objects.all()
    
    context = {
         'blog_posts': blog_posts
         }
    return render(request, 'blog.html', context )

