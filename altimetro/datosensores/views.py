from django.http import JsonResponse
from .models import TemperatureSensor
from django.shortcuts import render

def buscadatos(request):
    if request.method == 'GET':
        temperature = request.GET.get('temperature', None)
        if temperature:
            TemperatureSensor.objects.create(temperature=float(temperature))
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "message": "Temperature data missing."})
        
def display_data(request):
    data = TemperatureSensor.objects.all()
    return render(request, 'data_display.html', {'data': data})