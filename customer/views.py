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
    customerInfo = {
        "id": customer_id, 
        "vehicleInfo": Vehicle.objects.all,
        "reservationList":  Reservation.objects.all
    }
    return render(request, "customer/index.html", customerInfo)


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
    today = date.today()
    activeReservations = Reservation.objects.filter(userId=customer_id, startDate__lte=today, endDate__gte=today).values()
    pastReservations = Reservation.objects.filter(userId=customer_id, endDate__lt=today).values()
    futureReservations = Reservation.objects.filter(userId=customer_id, startDate__gt=today).values()

    context = {
        "activeReservations": filterReservations(activeReservations),
        "pastReservations": filterReservations(pastReservations),
        "futureReservations": filterReservations(futureReservations),
    }
    return render(request, "customer/rental.html", context)


def filterReservations(reservationObj):
    rentals = []
    reservations = []
    
    for reservation in reservationObj:
        rentals.append(Vehicle.objects.get(vehicleID=reservation.get('carId')))
        reservations.append(reservation)

    return zip(rentals, reservations)


# accesses the customer profile via the customer id and updates the moneyBalance field
# Redirects back to the vehicle page after the balance has been updated in the database
def addBalance(request, customer_id, vehicle_id):
    customer = Profile.objects.get(id=customer_id)

    add = request.POST.get('add')
    addedBalance = customer.moneyBalance + int(add)
    customer.moneyBalance = addedBalance
    customer.save()

    return HttpResponseRedirect(reverse('customer:vehiclePage', args=(customer_id, vehicle_id)))


# I know there has to be a better way of doing this, I just dont feel like doing it that way right now
def addBalanceHome(request, customer_id):
    customer = Profile.objects.get(id=customer_id)

    add = request.POST.get('add')
    addedBalance = customer.moneyBalance + int(add)
    customer.moneyBalance = addedBalance
    customer.save()

    return HttpResponseRedirect(reverse('customer:landingPage', args=(customer_id, )))


def cancelBooking(request, customer_id, vehicle_id, reservation_id):
    reservation = Reservation.objects.get(reservationId=reservation_id)
    reservation.delete()
    return HttpResponseRedirect(reverse('customer:viewRental', args=(customer_id, 0)))


def requestPickup(request, customer_id, vehicle_id, reservation_id):
    reservation = Reservation.objects.get(reservationId=reservation_id)
    reservation.needsPickup = True
    reservation.save()
    
    return HttpResponseRedirect(reverse('customer:viewRental', args=(customer_id, 0)))


