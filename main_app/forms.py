from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import Promocode, Rent

class RentingForm(ModelForm):
  class Meta:
    model = Rent
    fields = ['date','date','insurance','promocode']