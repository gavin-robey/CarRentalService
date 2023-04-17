from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vehicle
from .forms import *
from reservation.models import Reservation
from django.http import HttpResponseRedirect
from users.models import Profile

from .utils import Calendar
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe

def index(request):
  vehicles = Vehicle.objects.all()
  template = loader.get_template('employee/index.html')
  context = { 
    'vehicles': vehicles,
    'addHoursForm': addHours(request),
    }
  return HttpResponse(template.render(context, request))

class PickupItem():
  def __init__(self, pickupR, pickupV):
    self.carId = pickupR.carId
    self.endDate = pickupR.endDate
    self.location = pickupR.pickUpAddress
    self.make = pickupV.vehicleMake
    self.model = pickupV.vehicleModel
    self.year = pickupV.vehicleYear
  
def repo(request):
  pickupRs = Reservation.objects.filter(needsPickup=True)
  todayPickups = []
  futurePickups = []
  for pickupR in pickupRs.filter(endDate=datetime.today()):
    todayPickups.append(PickupItem(pickupR, Vehicle.objects.get(vehicleID=pickupR.carId)))
    
  for pickupR in pickupRs.filter(endDate__gt=datetime.today()):
    futurePickups.append(PickupItem(pickupR, Vehicle.objects.get(vehicleID=pickupR.carId)))
  template = loader.get_template('employee/repo.html')
  context = {
    'todayPickups':todayPickups,
    'futurePickups':futurePickups,
  }
  return HttpResponse(template.render(context, request))
  
def addVehicle(request):
  if request.method == 'POST':
    form = VehicleAddForm(request.POST, request.FILES)
    if form.is_valid():
      vid = addVehicleToDb(request)
      return HttpResponseRedirect('/employee/vehicle/' + str(vid))
  else:
    form = VehicleAddForm()
  
  return render(request, 'addVehicle.html', {'form':form})
  
def addVehicleToDb(request):
  v = Vehicle()
  v.vehicleYear = request.POST.get('vehicleYear')
  v.vehicleMake = request.POST.get('vehicleMake')
  v.vehicleModel = request.POST.get('vehicleModel')
  if 'vehicleImage' in request.FILES:
    v.vehicleImage = request.FILES['vehicleImage']
  v.vehiclePrice = request.POST.get('vehiclePrice')
  v.vehicleIsRetired = request.POST.get('vehicleIsRetired') == 'on'
  v.save()
  return v.vehicleID

def calendarView(request, vehicle_id, addMonths=0):
  d = get_date(request.GET.get('day', None))
  cal = Calendar(d.year, d.month)
  html_cal = cal.formatmonth(vehicle_id, addMonths, withyear=True)
  return mark_safe(html_cal)
  
def vehicleDetails(request, vehicle_id):
  template = loader.get_template('employee/vehicle.html')
  today = datetime.today()
  context = {}
  context['reservations'] = Reservation.objects.filter(carId=vehicle_id)
  context['calendarThis'] = calendarView(request, vehicle_id)
  context['calendarNext'] = calendarView(request, vehicle_id, addMonths=1)
  context['calendarNextNext'] = calendarView(request, vehicle_id, addMonths=2)
  context['vehicle'] = Vehicle.objects.get(pk=vehicle_id)
  context['todayReservation'] = Reservation.objects.filter(
    carId=vehicle_id,
    startDate__year=today.year,
    startDate__month=today.month,
    startDate__day=today.day)
  context['today'] = today

  return HttpResponse(template.render(context, request))

def customerDetails(request, customer_id):
  template = loader.get_template('employee/customer.html')
  context = {}
  context['user'] = Profile.objects.filter(user_id=customer_id)
  return HttpResponse(template.render(context, request))

def get_date(req_day):
  if req_day:
    year, month = (int(x) for x in req_day.split('-'))
    return date(year, month, day=1)
  return datetime.today()

def addHours(request):
  if request.method == 'POST':
    form = AddHoursForm(request.POST)
    if form.is_valid():
      p = request.user.profile
      request.user.profile.hoursWorked += int(request.POST.get('hoursWorked'))
      p.save()
  else:
    form = AddHoursForm()
  return form


def searchVehicle(request):
  return HttpResponse("Search for vehicles")


def addReservation(request, vehicle_id):
  if request.method == 'POST':
    form = ReservationAddForm(request.POST)
    if form.is_valid():
      r = addReservationToDb(request, vehicle_id)
      return HttpResponseRedirect('/employee/vehicle/' + str(vehicle_id))
  else:
    form = ReservationAddForm()
  return render(request, 'add_reservation.html', {'form':form, 'carId':vehicle_id})

def addReservationToDb(request, vehicle_id):
  r = Reservation()
  r.carId = vehicle_id
  r.userId = request.POST.get('userId')
  r.startDate = request.POST.get('startDate')
  r.endDate = request.POST.get('endDate')
  r.pickupAddress = request.POST.get('endDate')
  r.needsPickup = False
  r.hasInsurance = False #request.POST.get('hasInsurance')
  r.isReturned = True
  r.save()
