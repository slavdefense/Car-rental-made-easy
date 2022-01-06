from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/',views.about, name='about'),
  path('cars/',views.cars_index,name='cars_index'),
  path('cars/<int:car_id>/',views.cars_detail,name='cars_detail'),
  path('cars/create/',views.CarCreate.as_view(),name='cars_create'),
  path('cars/<int:pk>/update/',views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/',views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/rent/',views.cars_rent,name='cars_rent'),
  path('cars/<int:car_id>/add_rent',views.add_rent,name='add_rent'),
  path('promocode/create/',views.PromoCreate.as_view(),name='promos_create'),
  path('promocode/<int:pk>/',views.PromocodeDetail.as_view(),name='promocodes_detail'),
  path('promocode/',views.PromocodeList.as_view(),name='promocodes_index'),
  path('accounts/signup/', views.signup, name='signup'),
  path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),

  
  # path('cars/<int:user_id>/add_user',views.add_user,name='add_user'),
]

