from django.contrib import admin

# Register your models here.
from .models import Car, Rent
admin.site.register(Car)
admin.site.register(Rent)