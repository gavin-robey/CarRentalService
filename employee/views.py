from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vehicle
from .forms import VehicleAddForm
from django.http import HttpResponseRedirect

def index(request):
  vehicles = Vehicle.objects.all()
  template = loader.get_template('employee/index.html')
  context = {
    'vehicles': vehicles,
  }
  
  return HttpResponse(template.render(context, request))

def addVehicle(request):
  if request.method == 'POST':
    form = VehicleAddForm(request.POST, request.FILES)
    if form.is_valid():
      addVehicleToDb(request)
      return HttpResponseRedirect('/employee/vehicleDetails/')
  else:
    form = VehicleAddForm()
  
  return render(request, 'addVehicle.html', {'form':form})
  
  
def addVehicleToDb(request):
  v = Vehicle()
  # v.vehicleID = ??
  v.vehicleYear = request.POST.get('vehicleYear')
  v.vehicleMake = request.POST.get('vehicleMake')
  v.vehicleModel = request.POST.get('vehicleModel')
  if 'vehicleImage' in request.FILES:
    v.vehicleImage = request.FILES['vehicleImage']
  v.vehiclePrice = request.POST.get('vehiclePrice')
  v.vehicleIsRetired = request.POST.get('vehicleIsRetired') == 'on'
  
  v.save()
    
def vehicleAddConfirm(request):
  return HttpResponse("Confirmed adding vehicle!")

def vehicleDetails(request, vehicle_id):
  vehicle = Vehicle.objects.get(pk=vehicle_id)
  return HttpResponse(vehicle.vehicleMake)

def addCustomer(request):
  return HttpResponse("Add Customer")

def searchVehicle(request):
  return HttpResponse("Search for vehicles")
