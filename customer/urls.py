from django.urls import path
from . import views
import uuid

app_name = 'customer'
urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('<uuid:vehicle_id>/', views.vehiclePage, name='vehiclePage'),
    path('<uuid:vehicle_id>/submitRental/', views.submitRental, name='submitRental'),
    path('<int:vehicle_id>/viewRental/', views.viewRental, name="viewRental"),
    path('<uuid:vehicle_id>/addBalance/', views.addBalance, name="addBalance"),
]