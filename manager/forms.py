from django import forms
from employee.models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicleYear', 'vehicleMake', 'vehicleModel', 'vehicleImage', 'vehiclePrice', 'vehicleIsRetired']
        
    vehicleYear = forms.IntegerField(
        label='Year',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
        required=True
    )
    
    vehicleMake = forms.CharField(
        label='Make',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Make'}),
        max_length=64,
        required=True
    )
    
    vehicleModel = forms.CharField(
        label='Model',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model'}),
        max_length=64,
        required=True
    )
    
    vehicleImage = forms.ImageField(
        label='Image',
        # widget=forms.FileInput(attrs={'class': 'form-control-file'}),
        required=True
    )
    
    vehiclePrice = forms.IntegerField(
        label='Price',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
        required=True
    )
    
    vehicleIsRetired = forms.BooleanField(
        label='Is Retired',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )