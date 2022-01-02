from django.db import models
from django.urls import reverse

# Create your models here.
INSURANCES = (
  ('Y','Yes'),
  ('N','No')
)

class Car (models.Model):
  name = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  brand = models.TextField(max_length=250)
  mileage = models.IntegerField(blank = True)
  price = models.IntegerField(blank = True)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("cars_detail", kwargs={"car_id": self.id})
  
class Rent (models.Model):
  date=models.DateField()
  insurance = models.CharField(max_length=1,
    choices=INSURANCES,
    default=INSURANCES[0][0])

  car = models.ForeignKey(Car,on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_insurance_display()} on {self.date}"
  