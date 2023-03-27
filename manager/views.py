from django.shortcuts import render

# Create your views here.
def manager(request):
    context = {'name': 'Bob'}
    return render(request, 'manager.html', context)
