from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from employee.models import Vehicle
from .forms import VehicleForm


# Create your views here.
def manager(request):
    all_users= get_user_model().objects.all()
    all_vehicles = Vehicle.objects.all()

    
    context= {'allusers': all_users, 'allvehicles': all_vehicles}
    return render(request, 'manager.html', context)

def updateVehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicleID=vehicle_id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('/manager')

    context = {'vehicle': vehicle, 'form': form}
    return render(request, 'updateVehicle.html', context)

def createVehicle(request):
    # vehicle = Vehicle.objects.get(vehicleID=vehicle_id)
    form = VehicleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/manager')

    context = {'form': form}
    return render(request, 'createVehicle.html', context)
