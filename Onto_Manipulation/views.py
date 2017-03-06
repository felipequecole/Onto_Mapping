from django.shortcuts import render
from Onto_Manipulation import Onto_mapping



def index(request):
    dict = Onto_mapping.return_dict()
    return render(request, 'Onto_Manipulation/home.html', dict)

def edit(request):
    return render(request, 'Onto_Manipulation/edit.html', {})

def convert(request):
    return render(request, 'Onto_Manipulation/convert.html',{})

def download(request):
    return render(request, 'Onto_Manipulation/download.html', {})


# Create your views here.
