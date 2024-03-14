from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import CreateView,ListView, DetailView,UpdateView, DeleteView



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
    form_class = CarModelForm
    template_name = 'new_car.html'  
    success_url = '/car/'         


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/car/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/car/'