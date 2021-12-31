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
  Car('Lolo', 'Accord', 'Honda', 3000),
  Car('Sachi', 'Camry', 'Toyota', 1500),
  Car('Fancy', 'G37', 'Infinity', 400),
  Car('Bonk', 'M2', 'Bmw', 600),
]


def cars_index(request):
  return render(request,'cars/index.html',{'cars':cars})