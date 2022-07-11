from asyncio.windows_events import NULL
import json
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import About_us, Contact, Contact_us, Frieght_Type, Quote, Order, Service, Why_choose_us
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
import string

def home(request):
    context={
        "services": Service.objects.all(),
        "reasons": Why_choose_us.objects.all(),
        "freightTypes": Frieght_Type.objects.all(),
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

@csrf_exempt
def create_quote(request):
    data = json.loads(request.body)

    obj = Quote.objects.create(
        name = data['name'],
        email =data ['email'],
        phonenumber = data['phoneNumber'],
        freightType = Frieght_Type.objects.get(id=data['freightType']),
        departureCity = data['departureCity'],
        deliveryCite = data['deliveryCity'],
        height = data['height'],
        width = data['width'],
        length = data['length'],
        weight = data['weight'],
        fragile = data['fragile'],
        expressDelivery = data['expressDelivery'],
        insurance = data['insurance'],
        packaging = data['packaging'],
    )

    # code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
    # obj.code = code

    obj.save()

    return JsonResponse({},status=200)

@csrf_exempt
def create_contact(request):
    data = json.loads(request.body)

    obj = Contact.objects.create(
        name = data["name"],
        email = data["email"],
        phone_number = data["phoneNumber"],
        message = data["message"],
    )
    # code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
    # obj.code = code
    obj.save()
    return JsonResponse({},status=200)

