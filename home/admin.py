import imp
from django.contrib import admin
from home.models import webinars,therapies
# Register your models here.
admin.site.register(webinars)
admin.site.register(therapies)