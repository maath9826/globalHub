from django.shortcuts import render, redirect
from .forms import orderForm

from django.utils.crypto import get_random_string
import string


def index(request):
    order_form = orderForm()
    if request.method == 'POST':
        userform = orderForm(request.POST)
        if userform.is_valid():
            try:
                code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
                obj = userform.save(commit=False)
                obj.code = code
                obj.save()
            except:
                code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
                obj = userform.save(commit=False)
                obj.code = code
                obj.save()
            return redirect('index')

    return render(request, 'globalHub/index.html', context={
        'form': order_form
    })