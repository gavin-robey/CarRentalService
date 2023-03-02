from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vehicle

def index(request):
  vehicles = Vehicle.objects.all()
  template = loader.get_template('employee/index.html')
  context = {
    'vehicles': vehicles,
  }
  
  return HttpResponse(template.render(context, request))

def addCustomer(request):
  return HttpResponse("Add Customer")

def searchVehicle(request):
  return HttpResponse("Search for vehicles")
