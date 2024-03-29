from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', user_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('customer/<int:customer_id>/', include('customer.urls')), 
    path('rental/', include('rental.urls')), 
    path('register/', user_views.register, name='register'),
    path('employee/', include('employee.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('manager/', include('manager.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path("__reload__/", include("django_browser_reload.urls")), # for auto reloading of the server
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
