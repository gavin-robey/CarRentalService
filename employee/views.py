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
  
  
def addCustomer(request):
  return HttpResponse("Add Customer")

def searchVehicle(request):
  return HttpResponse("Search for vehicles")
