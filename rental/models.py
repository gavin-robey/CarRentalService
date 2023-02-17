from django.db import models

class Reservation(models.Model):
    
    reservationId = models.IntegerField()
    userId = models.CharField(max_length=200)
    carId = models.IntegerField()
    startDate = models.CharField(max_length=200)
    endDate = models.CharField(max_length=200)
    needsPickup = models.BooleanField()
    hasInsurance = models.BooleanField()
    pickUpAddress = models.CharField(max_length=200)
    isReturned = models.CharField(max_length=200)

    def __str__(self):
        return self.reservationId
