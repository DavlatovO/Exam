from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about_us'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),

]
