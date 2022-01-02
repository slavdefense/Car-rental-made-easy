from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Car,Promocode
from .forms import RentingForm


# Create your views here.
# from django.http import HttpResponse

# Define the home view



def home(request):
  return render(request, 'home.html')


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
  renting_form = RentingForm()
  return render(request,'cars/rent.html',{'car':car,'renting_form':renting_form})


