from django.shortcuts import render
from Onto_Manipulation import Onto_mapping
from django.views.decorators.csrf import csrf_exempt
import xmltodict
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
def edit_rel(request, id=""):
    if request.method == 'GET':
          if(id != "new"):
              ont = Onto_mapping.return_dict()
              for relation in ont['Ontology']['Relations']['Relation']:
                  if (relation['relationName'] == id):
                      relationDic = relation
          else:
              relationDic = {'@id': '', 'relationName': '', 'humanFormat': '', 'populate': '', 'visible': '', 'generalizations': '', 'domain': '', 'range': '', 'domainWithinRange': '', 'rangeWithinDomain': '', 'antireflexive': '', 'antisymmetric': '', 'mutexExceptions': '', 'knownNegatives': '', 'inverse': '', 'seedInstances': '', 'seedExtractionPatterns': '', 'nrOfValues': '', 'nrOfInverseValues': '', 'requiredForDomain': '', 'requiredForRange': '', 'queryString': '', 'editDate': '', 'author': '', 'curator': '', 'description': '', 'freebaseID': '', 'comment': ''}
    if request.method == 'POST':
        form = dict(request.POST)
        Onto_mapping.add_relation(form)
        relationDic = {'@id': '', 'relationName': '', 'humanFormat': '', 'populate': '', 'visible': '',
                       'generalizations': '', 'domain': '', 'range': '', 'domainWithinRange': '',
                       'rangeWithinDomain': '', 'antireflexive': '', 'antisymmetric': '', 'mutexExceptions': '',
                       'knownNegatives': '', 'inverse': '', 'seedInstances': '', 'seedExtractionPatterns': '',
                       'nrOfValues': '', 'nrOfInverseValues': '', 'requiredForDomain': '', 'requiredForRange': '',
                       'queryString': '', 'editDate': '', 'author': '', 'curator': '', 'description': '',
                       'freebaseID': '', 'comment': ''}
    return render(request, 'Onto_Manipulation/edit_rel.html', {'relation': relationDic})

def convert(request):
    return render(request, 'Onto_Manipulation/convert.html',{})

def download(request):
    return render(request, 'Onto_Manipulation/download.html', {})


# Create your views here.
