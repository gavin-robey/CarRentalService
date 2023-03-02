from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('addcustomer/', views.addCustomer, name='addcustomer'),
  path('searchvehicle/', views.searchVehicle, name='searchvehicle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-uploaded-files-in-development
# https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-MEDIA_URL
