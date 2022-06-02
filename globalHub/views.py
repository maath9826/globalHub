from django.shortcuts import render

def home(request):
    context={}
    return render(request, "globalHub/home.html",context)

def contact(request):
    context={}
    return render(request, "globalHub/contact.html",context)

def about(request):
    context={}
    return render(request, "globalHub/about.html",context)

def services(request):
    context={}
    return render(request, "globalHub/services.html",context)

def offers(request):
    context={}
    return render(request, "globalHub/offers.html",context)
# Create your views here.
