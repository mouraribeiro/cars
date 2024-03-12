from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarsModelForm
from django.views import View
from django.views.generic.list import ListView


# Create your views here.



class CarsView(View):
    
    def get(self,request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return render(request, 'cars.html', {'cars': cars})
        

# class CarsListView(ListView):
#     model = Car
#     template_name = 'cars.html'
#     context_object_name = 'cars'
   
    
class NewCarView(View):
    def get(self,request):
        new_car_form = CarsModelForm()
        return render(request, 'new_car.html', {'new_car_form':new_car_form})
        
    def post(self,request):
        new_car_form = CarsModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form':new_car_form})   
        
        