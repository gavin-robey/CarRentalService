from django.shortcuts import render
from django.contrib.auth import get_user_model


# Create your views here.
def manager(request):
    all_users= get_user_model().objects.all()
    
    context= {'allusers': all_users}
    return render(request, 'manager.html', context)
