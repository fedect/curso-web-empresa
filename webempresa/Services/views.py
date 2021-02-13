from django.shortcuts import render
from .models import Services

def servicio(request):
    services = Services.objects.all
    return render (request, "Services/services.html", {
        'services' : services
    })