from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)


class OrderAdminSite(admin.ModelAdmin):
    model = Order
    fields = [
        'user_name',
        'user_phone_number',
        'user_email',
        'order_info',
        'official_code',
        'code',
        'done'
    ]
    actions = ["Done"]

    list_display = ("user_name", "user_phone_number", "user_email", "order_info", "done")
    list_filter = ("user_name", "done")

    def Done(self, request, queryset):
        queryset.update(code=None, done=True)


# Register your models here.
admin.site.register(Order, OrderAdminSite)
admin.site.register(Service)
admin.site.register(Happy_Customer)
admin.site.register(Feedback)
admin.site.register(Branch)
admin.site.register(Staff)
admin.site.register(Offer)
admin.site.register(Why_choose_us)
admin.site.register(About_us)
admin.site.register(Logistics_solution)
admin.site.register(Contact_us)
admin.site.register(Quote)