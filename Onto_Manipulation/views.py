from django.shortcuts import render
from Onto_Manipulation import Onto_mapping
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import xmltodict
import os



def index(request):
    dict = Onto_mapping.return_dict()
    return render(request, 'home.html', dict)

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
        return render(request, 'Onto_Manipulation/sucess.html')
    return render(request, 'Onto_Manipulation/edit_cat.html', {})

@csrf_exempt
def edit_rel(request, id=""):
    relationDic = {'@id': '', 'relationName': '', 'humanFormat': '', 'populate': '', 'visible': '',
                   'generalizations': '', 'domain': '', 'range': '', 'domainWithinRange': '', 'rangeWithinDomain': '',
                   'antireflexive': '', 'antisymmetric': '', 'mutexExceptions': '', 'knownNegatives': '', 'inverse': '',
                   'seedInstances': '', 'seedExtractionPatterns': '', 'nrOfValues': '', 'nrOfInverseValues': '',
                   'requiredForDomain': '', 'requiredForRange': '', 'queryString': '', 'editDate': '', 'author': '',
                   'curator': '', 'description': '', 'freebaseID': '', 'comment': ''}
    ont = Onto_mapping.return_dict()
    for relation in ont['Ontology']['Relations']['Relation']:
        if (relation['relationName'] == id):
            relationDic = relation

    if request.method == 'POST':
        form = dict(request.POST)
        if(id == 'new'):
            Onto_mapping.add_relation(form)
            return render(request, 'Onto_Manipulation/sucess.html', {})
        else:
            Onto_mapping.edit_relation(form, relationDic['@id'])
            return render(request, 'Onto_Manipulation/sucess.html')

        relationDic = form

    return render(request, 'Onto_Manipulation/edit_rel.html', {'relation': relationDic})

def convert(request):
    return render(request, 'Onto_Manipulation/convert.html',{})

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
    pwd = os.path.dirname(__file__)
    file_path = os.path.join(pwd, 'static/Onto_Manipulation/data/relations.xls')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/xls")
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


    return render(request, 'Onto_Manipulation/convert.html', {})

# Create your views here.
