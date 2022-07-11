from django.urls import path

from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('services/<int:number>',views.services_parameter, name='services_parameter'),
    path('about',views.about, name='about'),
    path('offers',views.offers, name='offers'),
    path("quote/create", views.create_quote, name="create_quote"),
    path("contact/create", views.create_contact, name="create_contact")
]
