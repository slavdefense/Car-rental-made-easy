from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Car,Promocode
from .forms import ProfileForm, RentingForm
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# from django.http import HttpResponse

# Define the home view


class Home(LoginView):
  template_name = 'home.html'



def about(request):
  return render(request, 'about.html')


def cars_index(request):
  cars = Car.objects.all()
  return render(request,'cars/index.html',{'cars':cars})


def cars_detail(request,car_id):
  car = Car.objects.get(id=car_id)
  return render(request,'cars/detail.html',{'car':car})


def add_rent(request,car_id):


  form = RentingForm(request.POST)

  if form.is_valid():
    new_rent=form.save(commit=False)
    new_rent.car_id=car_id
    new_rent.save()
  return redirect('cars_rent',car_id=car_id)


class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class CarUpdate(UpdateView):
  model =  Car
  fields= '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url='/cars/'

class PromoCreate(CreateView):
  model = Promocode
  fields='__all__'

def cars_rent(request,car_id):
  car=Car.objects.get(id=car_id)
  profile_form=ProfileForm(request.POST)
  renting_form = RentingForm()
  if profile_form.is_valid(): 
      # do stuff here
      # form = ProfileForm(request.POST)
        new_profile = profile_form.save(commit=False)
        new_profile.car_id = car_id
        new_profile.user_id = request.user.id
        new_profile.save()
      # do stuff here
  if renting_form.is_valid():   
      # form = rentingForm(request.POST)
        new_renting = renting_form.save(commit=False)
        new_renting.car_id = car_id
        new_renting.user_id = request.user
        new_renting.creator = request.user
        new_renting.save()
  

  return render(request,'cars/rent.html',{'car':car,'renting_form':renting_form,'profile_form':profile_form})


class PromocodeList(ListView):
  model = Promocode

class PromocodeDetail(DetailView):
  model=Promocode

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('cars_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)



