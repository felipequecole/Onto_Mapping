from django.shortcuts import render
from Onto_Manipulation import Onto_mapping
from django.views.decorators.csrf import csrf_exempt
import xml.etree.ElementTree as etree
import os

def relation(request):
    dict = Onto_mapping.return_dict()
    return render(request, 'Onto_Manipulation/home_rel.html', dict)

def category(request):
    dict = Onto_mapping.return_dict()
    return render(request, 'Onto_Manipulation/home_cat.html', dict)

def edit(request):
    return render(request, 'Onto_Manipulation/edit.html', {})

@csrf_exempt
def edit_cat(request):
    if request.method == 'POST':
        form = dict(request.POST)
        Onto_mapping.add_category(form)
    return render(request, 'Onto_Manipulation/edit_cat.html', {})

@csrf_exempt
def edit_rel(request):
    if request.method == 'POST':
        form = dict(request.POST)
        Onto_mapping.add_relation(form)
    return render(request, 'Onto_Manipulation/edit_rel.html', {})

def convert(request):
    return render(request, 'Onto_Manipulation/convert.html',{})

def download(request):
    return render(request, 'Onto_Manipulation/download.html', {})


# Create your views here.
