from django.db import models
from django.urls import reverse

# Create your models here.


class Car (models.Model):
  name = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  brand = models.TextField(max_length=250)
  mileage = models.IntegerField(blank = True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("cars_detail", kwargs={"car_id": self.id})
  