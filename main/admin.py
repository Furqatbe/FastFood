from urllib.request import CacheFTPHandler
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Slider)
admin.site.register(News)
admin.site.register(Info)
admin.site.register(ContactUs)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)