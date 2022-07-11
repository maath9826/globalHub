from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)


class OrderAdminSite(admin.ModelAdmin):
    model = Order
    fields = [
        'branch',
        'user_name',
        'user_phone_number',
        'user_email',
        'order_info',
        # 'official_code',
        # 'code',
        'done'
    ]
    actions = ["Done"]

    list_display = ("user_name", "user_phone_number", "user_email", "order_info", "date", "done")
    list_filter = ("user_name", "done")

    def Done(self, request, queryset):
        queryset.update(code=None, done=True)
        
class Contact_View(admin.ModelAdmin):
    model = Contact
    fields = [
        'name',
        'phone_number',
        'email',
        'message',
        'done'
    ]
    actions = ["Done"]

    list_display = ("name", "phone_number", "email", "message", "date", "done")
    list_filter = ("name", "done")

    def Done(self, request, queryset):
        queryset.update(code=None, done=True)


class Quote_View(admin.ModelAdmin):
    model = Quote
    fields = [
        'name',
        'email',
        'phonenumber',
        'freightType',
        'departureCity',
        'deliveryCite',
        'height',
        'width',
        'length',
        'weight',
        'fragile',
        'expressDelivery',
        'insurance',
        'packaging',
        # 'code',
        # 'official_Code',
        'done'
    ]
    list_display = ("name", "email", "phonenumber", "freightType", 'date', "done")
    list_filter = ("name", "done")

    actions = ["Done"]

    def Done(self, request, queryset):
        queryset.update(code=None, done=True)


class Service_view(admin.ModelAdmin):
    model = Service
    fields = [
        'name_of_service',
        'description_of_service',
        'image_url',
        'icon_url',
        # 'image_for_service',
    ]
    list_display = ("name_of_service", "description_of_service")


class Feedback_View(admin.ModelAdmin):
    model = Feedback
    fields = [
        'name',
        'email',
        'content_of_feedback'
    ]
    list_display = ('name', 'email', 'content_of_feedback', 'date')


class Offer_View(admin.ModelAdmin):
    model = Offer
    fields = [
        'name_of_offer',
        'description_of_offer',
        'image_of_offer'
    ]
    list_display = ('name_of_offer', 'description_of_offer')


class Logistics_View(admin.ModelAdmin):
    model = Logistics_solution
    fields = [
        'name',
        'description',
        'image'
    ]
    list_display = ('name', 'description')


class Contact_view(admin.ModelAdmin):
    model = Contact_us
    fields = [
        'email',
        'phone_number',
        'facebook_url',
        'instagram_url',
        'telegram_url',
    ]
    list_display = ("email", 'phone_number')


admin.site.register(Order, OrderAdminSite)
admin.site.register(Contact, Contact_View)
admin.site.register(Quote, Quote_View)
admin.site.register(Service, Service_view)
admin.site.register(Feedback, Feedback_View)
admin.site.register(Branch)
admin.site.register(Offer, Offer_View)
admin.site.register(Why_choose_us)
admin.site.register(About_us)
admin.site.register(Logistics_solution, Logistics_View)
admin.site.register(Contact_us, Contact_view)

admin.site.register(Frieght_Type)
