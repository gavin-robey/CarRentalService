from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # in order to go to customer page, pass in customer id to url
    path('customer/<int:customer_id>/', include('customer.urls')), 
    path('rental/', include('rental.urls')),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
