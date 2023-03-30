from django import forms

class VehicleAddForm(forms.Form):
  vehicleYear = forms.IntegerField(label="Year", max_value=2023, min_value=1900)
  vehicleMake = forms.CharField(label="Make", max_length=64)
  vehicleModel = forms.CharField(label="Model", max_length=64)
  vehicleImage = forms.ImageField(label="Image")
  vehiclePrice = forms.IntegerField(label="Price")
  vehicleIsRetired = forms.BooleanField(label="Retired", required=False)

class AddHoursForm(forms.Form):
  hoursWorked = forms.IntegerField(label="Hours", max_value=24, min_value=1)
