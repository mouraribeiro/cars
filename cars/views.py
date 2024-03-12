from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarsModelForm
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import CreateView


# Create your views here.  

class CarsListView(ListView):    
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search) #unaccent' ajuda mas só com postgres
        return queryset
   

        
class NewCarCreateView(CreateView):
    
    model = Car
    form_class = CarsModelForm
    template_name = 'new_car.html'  
    success_url = '/cars/'         