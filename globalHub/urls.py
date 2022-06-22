from django.urls import path

from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('services/<int:number>',views.services_parameter, name='services_parameter'),
    path('about',views.about, name='about'),
    path('offers',views.offers, name='offers'),
    path("Home/saveQuote", views.Quote_save, name="saveQuote"),
    path("Contact/saveContact", views.Contact_save, name="saveOrder")
]
