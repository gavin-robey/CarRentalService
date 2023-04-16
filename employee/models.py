import uuid
from django.db import models

class Vehicle(models.Model):
  vehicleID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  vehicleYear = models.IntegerField()
  vehicleMake = models.CharField(max_length=64)
  vehicleModel = models.CharField(max_length=64)
  vehicleImage = models.ImageField(upload_to='vehicles') # Requires Pillow
  vehicleImage2 = models.ImageField(upload_to='vehicles', blank=True)
  vehicleImage3 = models.ImageField(upload_to='vehicles', blank=True)
  vehicleImage4 = models.ImageField(upload_to='vehicles', blank=True)

  vehiclePrice = models.IntegerField()
  vehicleIsRetired = models.BooleanField(default=False)
  
  def __str__(self):
    return str(self.vehicleYear) + " " + str(self.vehicleMake) + " " + str(self.vehicleModel)
