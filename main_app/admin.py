from django.contrib import admin

# Register your models here.
from .models import Car, Rent,Promocode
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Promocode)