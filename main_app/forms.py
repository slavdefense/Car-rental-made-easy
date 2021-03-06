from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import Promocode, Rent
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class RentingForm(ModelForm):
  class Meta:
    model = Rent
    fields = ['sdate','edate','insurance','promocode','imageurl']


class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = [ 'address1', 'city', 'state', 'zipcode']

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)