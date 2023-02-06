from django.contrib import admin
from django.urls import include, path

from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', include('rental.urls')),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
]
