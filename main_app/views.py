from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>List your car for rent</h1>')


def about(request):
  return HttpResponse('<h3> This is the response</h3>')