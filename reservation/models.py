import uuid
from django.db import models

class Reservation(models.Model):
    reservationId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carId = models.IntegerField()
    userId = models.IntegerField()
    startDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    endDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    pickUpAddress = models.CharField(max_length=300) #can change to actual address model later
    needsPickup = models.BooleanField()
    hasInsurance = models.BooleanField()
    isReturned = models.BooleanField()

    def __UUID__(self):
        return self.reservationId
