from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import Rent

class RentingForm(ModelForm):
  class Meta:
    model = Rent
    fields = ['date','insurance']