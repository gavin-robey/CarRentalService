from django.shortcuts import render

def landingPage(request, customer_id):
    return render(request, "customer/index.html", { "id": customer_id, })
