from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,FormView
from django.http import HttpResponse
from App.models import *

class DataInList(ListView):
    model=Trainer
    template_name='DataInList.html'
    context_object_name='tl'
    # queryset=Trainer.objects.filter(name='')
    ordering=['name']