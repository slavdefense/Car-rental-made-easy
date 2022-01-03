from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import Promocode, Rent
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RentingForm(ModelForm):
  class Meta:
    model = Rent
    fields = ['date','date','insurance','promocode']


# class ProfileForm(ModelForm):
#   class Meta:
#     model = Profile
#     fields = ['phone', 'address1', 'city', 'state', 'zipcode']