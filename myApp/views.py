from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from myApp.models import Beer

# Create your views here.
class BeerListView(ListView):

    model = Beer

class BeerDetailView(DetailView):

    model = Beer

class BeerCreateView(CreateView):

    model = Beer
    fields = '__all__'

class BeerUpdateView(UpdateView):

    model = Beer
    fields = ['teste', 'color', 'price']

class BeerDeleteView(DeleteView):

    model = Beer
    success_url = reverse_lazy('home')
