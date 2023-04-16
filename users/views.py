
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


# Ensures a user is authenticated before checking the role of the user
def home(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "user":
            return HttpResponseRedirect(reverse('customer:landingPage', args=(request.user.profile.id,)))
        elif request.user.profile.role == "employee":
            return HttpResponseRedirect(reverse("employee:index"))
        else:
            return HttpResponseRedirect(reverse("manager:manager"))
    else:
        return HttpResponseRedirect(reverse('login'))


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
