from django.shortcuts import render
from .models import Business
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.


class BusinessCreateView(CreateView):
    model = Business
    template_name = 'business_new.html'
    fields = '__all__'


class BusinessCardView(ListView):
    model = Business
    template_name = 'business_card.html'

