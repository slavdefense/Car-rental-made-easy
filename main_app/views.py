from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Car,Promocode
from .forms import ProfileForm, RentingForm
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Rent,Photo
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'my-cat-collector-very-happy'
# from django.contrib.auth.models import User
# Create your views here.
# from django.http import HttpResponse

# Define the home view


class Home(LoginView):
  template_name = 'home.html'



def about(request):
  return render(request, 'about.html')


def cars_index(request):
  print('index page!')
  cars = Car.objects.all()
  return render(request,'cars/index.html',{'cars':cars})


def cars_detail(request,car_id):
  car = Car.objects.get(id=car_id)
  return render(request,'cars/detail.html',{'car':car})


def add_rent(request,car_id):
  
  # car=Car.objects.get(id=car_id)
  form = RentingForm(request.POST)

  if form.is_valid():
    new_rent=form.save(commit=False)
    new_rent.car_id=car_id
    # new_rent.user_id=user_id
    new_rent.save()
    
  return redirect('cars_rent',car_id=car_id)
  


# def add_user(request,car_id,user_id):
  
#   # car=Car.objects.get(id=car_id)
#   form = ProfileForm(request.POST)

#   if form.is_valid():
#     new_user=form.save(commit=False)
#     new_user.car_id=car_id
#     new_user.user_id=user_id
#     new_user.save()
    
#   return redirect('cars_rent',car_id=car_id,user_id=user_id)
 











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
  
  # print('hi')
  car=Car.objects.get(id=car_id)


  
  profile_form=ProfileForm(request.POST)
 
  renting_form = RentingForm(request.POST)
  renter = request.user
  print(renter)
  # new_renting = renting_form.save(commit=False)
  # new_renting.creator = request.user
  # new_renting.save()
  # print(new_renting.creator)
  if profile_form.is_valid(): 
    
        new_profile = profile_form.save(commit=False)
        new_profile.car_id = car_id
        new_profile.user_id = request.user.id
        new_profile.save()
  if renting_form.is_valid():   
       
        new_renting = renting_form.save(commit=False)
        new_renting.car_id = car_id
        new_renting.user_id = request.user
        new_renting.creator = request.user
        new_renting.save()
         
  return render(request,'cars/rent.html',{'car':car,'renting_form':renting_form,'profile_form':profile_form,'renter':renter})











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


# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#       # This will add the user to the database
#       user = form.save()
#       user.refresh_from_db()
#       user.username = user.email
#       user.profile.first_name = form.cleaned_data.get('first_name')
#       user.profile.last_name = form.cleaned_data.get('last_name')
#       user.profile.email = form.cleaned_data.get('email')
#       user.save()
#       login(request, user)
#       # This is how we log a user in via code
#       # login(request, user)
#       return redirect('index')
#     else:
#       error_message = 'Invalid sign up - try again'
#   # A bad POST or a GET request, so render signup.html with an empty form
#   form = SignUpForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)
def add_photo(request, car_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, car_id=car_id)
      # Remove old photo if it exists
      car_photo = Photo.objects.filter(car_id=car_id)
      if car_photo.first():
        car_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('cars_detail', car_id=car_id)