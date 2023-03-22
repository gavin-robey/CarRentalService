from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from reservation.models import Reservation
from users.models import Profile
from employee.models import Vehicle
from django.contrib.auth.models import User
from datetime import date


def landingPage(request, customer_id):
    # Code to only display vehicles available today
    # Don't actually think we need this feature but keeping the code just in case
    # today = date.today()
    # reservations = Reservation.objects.filter(startDate__lt=today, endDate__gt=today)
    # available = []
    
    # for reservation in reservations:
    #     available.append(reservation.carId)

    # vehicles = Vehicle.objects.filter().exclude(pk__in=available)
    return render(request, "customer/index.html", {"vehicleInfo": Vehicle.objects.all, "reservationList":  Reservation.objects.all})


def vehiclePage(request, customer_id, vehicle_id):
    vehicle = Vehicle.objects.get(vehicleID=vehicle_id)
    vehicleInfo = { 
                "id": customer_id, 
                "vehicleInfo" : vehicle,  
                "reserved": Reservation.objects.filter(carId=vehicle_id)
            }
    return render(request, "customer/vehicle.html", vehicleInfo)


# Updates reservation object in the database with customer data
# Subtracts total cost from the customer balance
def submitRental(request, customer_id, vehicle_id):
    reservation = Reservation()
    customer = Profile.objects.get(id=customer_id)

    startDate = datetime.strptime(request.POST.get('startDate'), '%Y-%m-%d').date()
    endDate = datetime.strptime(request.POST.get('endDate'), '%Y-%m-%d').date()

    for reserved in Reservation.objects.filter(carId=vehicle_id):
        if reserved.startDate <= startDate <= reserved.endDate or reserved.startDate <= endDate <= reserved.endDate:
            return HttpResponseRedirect(reverse('customer:vehiclePage', args=(customer_id, vehicle_id)))

    pickUpAddress = request.POST.get('pickUpAddress')
    hasInsurance = request.POST.get('hasInsurance', False)
    totalCost = request.POST.get('totalCost')

    if hasInsurance == 'on':
        hasInsurance = True
    else:
        hasInsurance = False

    reservation.carId = vehicle_id
    reservation.userId = customer_id
    reservation.startDate = startDate
    reservation.endDate = endDate
    reservation.pickUpAddress = pickUpAddress
    reservation.needsPickup = False
    reservation.hasInsurance = hasInsurance
    reservation.isReturned = False

    customer.moneyBalance -= int(totalCost)

    reservation.save()
    customer.save()

    return HttpResponseRedirect(reverse('customer:viewRental', args=(customer_id, 0)))


def viewRental(request, customer_id, vehicle_id):
    reservationObj = Reservation.objects.filter(userId=customer_id).values()
    rentals = []
    reservations = []

    customer = Profile.objects.get(id=customer_id)

    for reservation in reservationObj:
        rentals.append(Vehicle.objects.get(vehicleID=reservation.get('carId')))
        reservations.append(reservation)

    resDetails = zip(rentals, reservations)
    return render(request, "customer/rental.html", {"resDetails" : resDetails, "balance": customer.moneyBalance })



# accesses the customer profile via the customer id and updates the moneyBalance field
# Redirects back to the vehicle page after the balance has been updated in the database
def addBalance(request, customer_id, vehicle_id):
    customer = Profile.objects.get(id=customer_id)

    add = request.POST.get('add')
    addedBalance = customer.moneyBalance + int(add)
    customer.moneyBalance = addedBalance

    customer.save()

    return HttpResponseRedirect(reverse('customer:vehiclePage', args=(customer_id, vehicle_id)))





