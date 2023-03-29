from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('addvehicle/', views.addVehicle, name='addVehicle'),
  path('addcustomer/', views.addCustomer, name='addcustomer'),
  path('searchvehicle/', views.searchVehicle, name='searchvehicle'),
  path('vehicle/<str:vehicle_id>/', views.vehicleDetails, name='vehicleDetails'),
]

# https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-uploaded-files-in-development
# https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-MEDIA_URL
