from django.contrib import admin
from .models import register
from front.models import student,payment,paystatus

# Register your models here.
admin.site.register(register),
admin.site.register(student),
admin.site.register(payment),
admin.site.register(paystatus)