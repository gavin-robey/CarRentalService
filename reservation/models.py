from django.db import models

class Reservation(models.Model):
    reservationId = models.IntegerField()
    carId = models.IntegerField()
    userId = models.IntegerField()
    startDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    endDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    pickUpAddress = models.CharField(max_length=30) #can change to actual address model later
    needsPickup = models.BooleanField()
    hasInsurance = models.BooleanField()
    isReturned = models.BooleanField()

    def __str__(self):
        return self.reservationId
