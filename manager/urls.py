from django.urls import path
from . import views
import uuid

app_name = 'manager'
urlpatterns = [  
    path('', views.manager, name="manager"),
    path('update_vehicle/<uuid:vehicle_id>', views.updateVehicle, name="update-vehicle"),
    path('create_vehicle', views.createVehicle, name="create-vehicle"),
]