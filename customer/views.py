from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from reservation.models import Reservation

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
    # simulates customer information for given customer
    customerInfo = {
        "userId": customer_id,
        "email": "exampleEmail@gmail.com",
        "password": "helloworld",
        "moneyBalance": 124,
        "role": "customer",
        "hoursWorked": 0,
    }

    return render(request, "customer/index.html", { "customerInfo": customerInfo, "vehicleInfo": vehicleInfo})


def vehiclePage(request, customer_id, vehicle_id):
    vehicle = getVehicle(vehicle_id)
    return render(request, "customer/vehicle.html", { "customerId": customer_id, "vehicleInfo" : vehicle})


def submitRental(request, customer_id, vehicle_id):
    reservation = Reservation()

    startDate = request.POST.get('startDate')
    endDate = request.POST.get('endDate')
    pickUpAddress = request.POST.get('pickUpAddress')
    hasInsurance = request.POST.get('hasInsurance', False)

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

    reservation.save()

    return HttpResponseRedirect(reverse('customer:viewRental', args=(customer_id, vehicle_id)))

# simulates querying the database of cars
def getVehicle(vehicle_id):
    currentVehicle = None
    for vehicle in vehicleInfo:
        if vehicle["carId"] == vehicle_id:
            currentVehicle = vehicle

    return currentVehicle


def viewRental(request, customer_id, vehicle_id):
    rentals = []
    reservations = Reservation.objects.filter(userId=customer_id).values()
    
    for reservation in reservations:
        rentals.append(getVehicle(reservation.get('carId')))
    
    return render(request, "customer/rental.html", {"reservations" : reservations, "rentals": rentals })



