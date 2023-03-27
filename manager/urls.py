from django.urls import path
from . import views
import uuid

app_name = 'manager'
urlpatterns = [  
    path('', views.manager, name="manager"),
]