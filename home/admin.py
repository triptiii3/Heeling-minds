import imp
from django.contrib import admin
from home.models import  enquiry,therapies
# Register your models here.
admin.site.register(enquiry)
admin.site.register(therapies)
