from .models import Order
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class orderForm(forms.ModelForm):
    user_phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IQ',
                                       attrs={
                                           'placeholder': ('Phone number'),
                                               'class': "form-control",
                                           'style': 'margin: 5px 0 5px 10px;'
                                                    'width:auto;'
                                                    'display:inline;'
                                              }
                                       )
    )

    class Meta:
        model = Order
        fields = [
            'user_name',
            'user_email',
            'user_phone_number',
            'order_info'
        ]

        widgets = {
            'order_info': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'placeholder': "enter the details of your order"
                }
            ),
            'user_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "enter username",
                    'style': 'margin: 5px 0 5px 10px;'
                             'width:auto;'
                }
            ),
            'user_email': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "enter username",
                    'style': 'margin: 5px 0 5px 10px;'
                             'width:auto;'
                }
            ),
            'user_phone_number': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "enter phone number",
                    'style': 'margin: 5px 0 5px 10px;'
                             'width:auto;'
                }
            ),
        }
