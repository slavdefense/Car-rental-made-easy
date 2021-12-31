from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'base.html')


def about(request):
  return render(request, 'about.html')

# Add the Car class & list and view function below the imports
class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, model, brand, mileage):
    self.name = name
    self.model = model
    self.brand = brand
    self.mileage = mileage

cars = [
  Car('Sagun', 'Accord', 'Honda', 3000),
  Car('Dipa', 'Camry', 'Toyota', 1500),
  Car('Ben', 'G37', 'Infinity', 400),
  Car('Jurgen', 'Leaf', 'Nissan', 600),
  Car('Erik', 'Fx', 'Tesla', 5500),
  Car('Elon', 'M2', 'Bmw', 6500),
  Car('Patricia', 'M3', 'Bmw', 6500),
  Car('Rajesh', 'Escape', 'Ford', 3300),
  Car('Durg', 'Tahoe', 'Chevy', 7700),
  Car('Fancy', 'Miata', 'Mazda', 400),
  Car('Jordan', 'xod', 'Hummer', 6700),
  Car('Jira', 'fast', 'Ferrari', 11100),
  Car('Som', 'Veneno', 'Lamborgini', 2200),
]


def cars_index(request):
  return render(request,'cars/index.html',{'cars':cars})