from django.shortcuts import render, redirect
from Onto_Manipulation import Onto_mapping
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import xmltodict
import os


working_ontology = 'ontology.xml'

def index(request):
    global working_ontology
    dict = Onto_mapping.return_dict(working_ontology)
    list = Onto_mapping.list_ontologies()
    context = {'ontology': dict, 'list': list}
    return render(request, 'home.html', context)

def relation(request):
    global working_ontology
    list = Onto_mapping.list_ontologies()
    dict = Onto_mapping.return_dict(working_ontology)
    dict['list'] = list
    return render(request, 'Onto_Manipulation/home_rel.html', dict)

def category(request):
    global working_ontology
    list = Onto_mapping.list_ontologies()
    dict = Onto_mapping.return_dict(working_ontology)
    dict['list'] = list
    return render(request, 'Onto_Manipulation/home_cat.html', dict)

@csrf_exempt
def edit_cat(request):
    global working_ontology
    if request.method == 'POST':
        form = dict(request.POST)
        Onto_mapping.add_category(form, working_ontology)
        return render(request, 'Onto_Manipulation/sucess.html')
    return render(request, 'Onto_Manipulation/edit_cat.html', {})

@csrf_exempt
def edit_rel(request, id=""):
    global working_ontology
    relationDic = {'@id': '', 'relationName': '', 'humanFormat': '', 'populate': '', 'visible': '',
                   'generalizations': '', 'domain': '', 'range': '', 'domainWithinRange': '', 'rangeWithinDomain': '',
                   'antireflexive': '', 'antisymmetric': '', 'mutexExceptions': '', 'knownNegatives': '', 'inverse': '',
                   'seedInstances': '', 'seedExtractionPatterns': '', 'nrOfValues': '', 'nrOfInverseValues': '',
                   'requiredForDomain': '', 'requiredForRange': '', 'queryString': '', 'editDate': '', 'author': '',
                   'curator': '', 'description': '', 'freebaseID': '', 'comment': ''}
    ont = Onto_mapping.return_dict(working_ontology)
    for relation in ont['Ontology']['Relations']['Relation']:
        if (relation['relationName'] == id):
            relationDic = relation

    if request.method == 'POST':
        form = dict(request.POST)
        if(id == 'new'):
            Onto_mapping.add_relation(form, working_ontology)
            return render(request, 'Onto_Manipulation/sucess.html', {})
        else:
            Onto_mapping.edit_relation(form, relationDic['@id'], working_ontology)
            return render(request, 'Onto_Manipulation/sucess.html')

        relationDic = form

    list = Onto_mapping.list_ontologies()
    return render(request, 'Onto_Manipulation/edit_rel.html', {'relation': relationDic, 'list': list})

def convert(request):
    list = Onto_mapping.list_ontologies()
    return render(request, 'Onto_Manipulation/convert.html', {'list': list})

def download_XML(request):
    pwd = os.path.dirname(__file__)
    file_path = os.path.join(pwd, 'static/Onto_Manipulation/data/ontology.xml')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return render(request, 'Onto_Manipulation/download.html', {})


def download_XLS(request):
    Onto_mapping.create_xls()
    Onto_mapping.create_zip()
    pwd = os.path.dirname(__file__)
    file_path = os.path.join(pwd, 'static/Onto_Manipulation/data/ontology.zip')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/zip")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response



    return render(request, 'Onto_Manipulation/download.html', {})

def download(request):
    return render(request, 'Onto_Manipulation/download.html', {})


def upload_XML(request):
    if request.method=='POST' and request.FILES:
        pwd = os.path.dirname(__file__)
        filename = os.path.join(pwd, 'static/Onto_Manipulation/data/ontology.xml')
        xml_target = open(filename, 'wb')
        ontology = xmltodict.parse(request.FILES['xmlfile'])
        xmltodict.unparse(ontology, output=xml_target)


    return render(request, 'Onto_Manipulation/convert.html', {'list':Onto_mapping.list_ontologies()})

def select(request, id=""):
    if (id == 'default'):
        global working_ontology
        working_ontology = 'ontology.xml'
        print(working_ontology)
    else:
       global working_ontology
       working_ontology= id+'.xml'
       print(working_ontology)

    return redirect('/relation')

# Create your views here.
