from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.landingPage, name='landingPage'),
]