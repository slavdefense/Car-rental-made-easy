
from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User
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
  # car_image = models.ImageField(null=True,blank=True)

  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("cars_detail", kwargs={"car_id": self.id})
  
class Rent (models.Model):
  sdate=models.DateField()
  edate=models.DateField()
  imageurl = models.CharField(max_length=200,null=True)
 
  
  insurance = models.CharField(max_length=1,
    choices=INSURANCES,
    default=INSURANCES[0][0])
  promocode=models.CharField(max_length=15)
  car = models.ForeignKey(Car,on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

  def __str__(self):
    return f"{self.get_insurance_display()} insurance from {self.sdate} to {self.edate}"
  class Meta:
    ordering=['sdate']


class Promocode(models.Model):
  code = models.CharField(max_length=10)

  def __str__(self):
    return self.code
  
  def get_absolute_url(self):
      return reverse("promocodes_detail", kwargs={"pk": self.id})


class Profile(models.Model):
    # # admin view only???
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
      # Nice method for obtaining the friendly value of a Field.choice
      return f"ID#:{self.user.id} - {self.user.first_name} {self.user.last_name}"

class Meta:
        managed = False
        db_table = 'profile' 

class Photo(models.Model):
  url = models.CharField(max_length=250)
  car = models.OneToOneField(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for car_id: {self.car_id} @{self.url}"