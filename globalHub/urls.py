from django.urls import path, include
from . import views

urlpatterns = [


    # saveing forms URLS
    path("Home/saveQuote", views.Quote_save, name="saveQuote"),
    path("Contact/saveContact", views.Contact_save, name="saveOrder")
]
