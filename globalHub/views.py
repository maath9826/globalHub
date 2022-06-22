from asyncio.windows_events import NULL
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import About_us, Contact_us, Quote, Order, Service, Why_choose_us
from django.utils.crypto import get_random_string
import string

def home(request):
    context={
        "services": Service.objects.all(),
        "reasons": Why_choose_us.objects.all(),
    }
    return render(request, "globalHub/home.html",context)

def contact(request):
    context={}
    return render(request, "globalHub/contact.html",context)

def about(request):
    context={
        "content": About_us.objects.last().text
    }
    return render(request, "globalHub/about.html",context)

def services(request):
    context={
        "services": Service.objects.all(),
    }
    return render(request, "globalHub/services.html",context)

def services_parameter(request, number):
    context={
        "services": Service.objects.all(),
        "number": number
    }
    return render(request, "globalHub/services.html",context)

def offers(request):
    context={}
    return render(request, "globalHub/offers.html",context)

def send_message(request, sender, recipient, subject, content):
    send_mail(
        subject,
        content,
        sender,
        recipient,
        fail_silently=False,
    )


def Quote_save(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phoneNumber = request.POST.get("phoneNumber")
    # Add id or name for Freight Type in Html
    City_of_Departure = request.POST.get("departureCity")
    Delivery_City = request.POST.get("deliveryCity")
    height = request.POST.get("height")
    width = request.POST.get("width")
    length = request.POST.get("length")
    weight = request.POST.get("weight")
    # Add a unique name or ID for the last Booleans

    obj = Quote.objects.create(
        name=name,
        email=email,
        phonenumber=phoneNumber,
        # freightType=,
        departureCity=City_of_Departure,
        deliveryCite=Delivery_City,
        height=height,
        width=width,
        length=length,
        weight=weight,
        # fragile=,
        # expressDelivery=,
        # insurance=,
        # packaging=,
    )
    code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
    obj.code = code
    obj.save()
    # Add redirect after marge


def Contact_save(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phoneNumber = request.POST.get("phoneNumber")
    message = request.POST.get("message")

    obj = Order.objects.create(
        user_name=name,
        user_email=email,
        user_phone_number=phoneNumber,
        order_info=message,
    )
    code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
    obj.code = code
    obj.save()

