from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from reservation.models import Reservation
from users.models import Profile
from django.contrib.auth.models import User

# simulates the data base of vehicles 
vehicleInfo = [
    {
    "carId": 1,
    "make": "Volkswagen",
    "model": "Golf",
    "images": "example image", 
    "price": 50.00,
    "isRetired": False },

    {
    "carId": 2,
    "make": "Toyota",
    "model": "Camry",
    "images": "example image", 
    "price": 100.00,
    "isRetired": False },

    {
    "carId": 3,
    "make": "Chevrolet",
    "model": "Silverado",
    "images": "example image", 
    "price": 150.00,
    "isRetired": False },

    {
    "carId": 4,
    "make": "Lamborghini",
    "model": "Aventador",
    "images": "example image", 
    "price": 300.00,
    "isRetired": False },

    {
    "carId": 5,
    "make": "Ford",
    "model": "Pinto",
    "images": "example image", 
    "price": 25.00,
    "isRetired": False }
]

def landingPage(request, customer_id):
    return render(request, "customer/index.html", {"vehicleInfo": vehicleInfo})


def vehiclePage(request, customer_id, vehicle_id):
    vehicle = getVehicle(vehicle_id)
    return render(request, "customer/vehicle.html", { "id": customer_id, "vehicleInfo" : vehicle})


# Updates reservation object in the database with customer data
# Subtracts total cost from the customer balance
def submitRental(request, customer_id, vehicle_id):
    reservation = Reservation()
    customer = Profile.objects.get(id=customer_id)

    startDate = request.POST.get('startDate')
    endDate = request.POST.get('endDate')
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

    return HttpResponseRedirect(reverse('customer:viewRental', args=(customer_id, vehicle_id)))


# simulates querying the database of cars
def getVehicle(vehicle_id):
    currentVehicle = None
    for vehicle in vehicleInfo:
        if vehicle["carId"] == vehicle_id:
            currentVehicle = vehicle

    return currentVehicle


def viewRental(request, customer_id, vehicle_id):
    reservationObj = Reservation.objects.filter(userId=customer_id).values()
    rentals = []
    reservations = []

    customer = Profile.objects.get(id=customer_id)

    for reservation in reservationObj:
        # This will be useful to calculate if a rental is booked or not
        # d1 = reservation.get('startDate')
        # d2 = reservation.get('endDate')

        # days = (d2 - d1).days
        # print(days)

        rentals.append(getVehicle(reservation.get('carId')))
        reservations.append(reservation)

    # zip arrays so that both data sets can be displayed at the same time in the template
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





