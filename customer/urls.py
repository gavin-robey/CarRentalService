from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('<int:vehicle_id>/', views.vehiclePage, name='vehiclePage'),
    path('<int:vehicle_id>/submitRental/', views.submitRental, name='submitRental'),
    path('<int:vehicle_id>/viewRental/', views.viewRental, name="viewRental"),
    path('<int:vehicle_id>/addBalance/', views.addBalance, name="addBalance"),
]