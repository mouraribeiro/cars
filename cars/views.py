from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm


# Create your views here.


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})



def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarForm(request.POST)
        
    else:
        new_car_form = CarForm()
        return render(request, 'new_car.html', {'new_car_form':new_car_form})