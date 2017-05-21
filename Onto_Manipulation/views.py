from django.shortcuts import render, redirect
from Onto_Manipulation import Onto_mapping
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import xmltodict
from xlrd import open_workbook

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os


working_ontology = 'ontology.xml'

def get_working_ontology():
    global working_ontology
    return working_ontology

def set_working_ontology(_working_ontology: str):
    global working_ontology
    working_ontology = _working_ontology

def index(request):
    working_ontology = get_working_ontology()
    dict = Onto_mapping.return_dict(working_ontology)
    list = Onto_mapping.list_ontologies()
    context = {'ontology': dict, 'list': list}
    return render(request, 'Onto_Manipulation/home.html', context)

def relation(request):
    working_ontology = get_working_ontology()
    list = Onto_mapping.list_ontologies()
    dict = Onto_mapping.return_dict(working_ontology)
    dict['list'] = list
    return render(request, 'Onto_Manipulation/home_rel.html', dict)

def category(request):
    working_ontology = get_working_ontology()
    list = Onto_mapping.list_ontologies()
    dict = Onto_mapping.return_dict(working_ontology)
    dict['list'] = list
    return render(request, 'Onto_Manipulation/home_cat.html', dict)

@csrf_exempt
def edit_cat(request, id=""):
    working_ontology = get_working_ontology()
    categoryDic = {'@id': '', 'categoryName': '', 'englishName': '', 'humanFormat': '', 'populate': '',
                   'visible': '', 'domain': '', 'range': '', 'domainWithinRange': '', 'rangeWithinDomain': '',
                   'antireflexive': '', 'generalizations': '', 'mutexExceptions': '', 'knownNegatives': '', 'instanceType': '',
                   'seedInstances': '', 'seedExtractionPatterns': '', 'conceptSynonyms': '', 'queryString': '',
                   'editDate': '', 'author': '', 'curator': '', 'description': '', 'freebaseID': '', 'comment': ''}
    ont = Onto_mapping.return_dict(working_ontology)
    for category in ont['Ontology']['Categories']['Category']:
        if (category['categoryName'] == id):
            categoryDic = category


    if request.method == 'POST':
        form = dict(request.POST)
        if (id == 'new'):
            print(working_ontology)
            Onto_mapping.add_category(form, working_ontology)
            return render(request, 'Onto_Manipulation/sucess.html', {'new': '1'})
        else:
            Onto_mapping.edit_category(form, categoryDic['@id'], working_ontology)
            return render(request, 'Onto_Manipulation/sucess.html')

        categoryDic = form

    list = Onto_mapping.list_ontologies()
    if id == 'new':
        return render(request, 'Onto_Manipulation/edit_cat.html',
                      {'category': {'new': '1'}, 'list': list, 'cat': ont['Ontology']['Categories']['Category']})

    return render(request, 'Onto_Manipulation/edit_cat.html', {'category': categoryDic, 'list': list, 'cat':ont['Ontology']['Categories']['Category']})

@csrf_exempt
def edit_rel(request, id=""):
    working_ontology = get_working_ontology()
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
    cat = ont['Ontology']['Categories']['Category']
    rel = ont['Ontology']['Relations']['Relation']


    if request.method == 'POST':
        form = dict(request.POST)
        if(id == 'new'):
            Onto_mapping.add_relation(form, working_ontology)
            return render(request, 'Onto_Manipulation/sucess.html', {'list': Onto_mapping.list_ontologies()})
        else:
            Onto_mapping.edit_relation(form, relationDic['@id'], working_ontology)
            return render(request, 'Onto_Manipulation/sucess.html', {'list': Onto_mapping.list_ontologies()})

        relationDic = form

    context = {'relation':relationDic, 'categories':cat, 'rel':rel}

    list = Onto_mapping.list_ontologies()
    if (id == 'new'):
        return render(request, 'Onto_Manipulation/edit_rel.html', { 'new': '1', 'list': list, 'ontology': context})
    return render(request, 'Onto_Manipulation/edit_rel.html', {'ontology': context, 'list': list})


def convert(request):
    list = Onto_mapping.list_ontologies()
    return render(request, 'Onto_Manipulation/convert.html', {'list': list})

def download_XML(request):
    pwd = os.path.dirname(__file__)
    file_path = os.path.join(pwd, 'data/ontology.xml')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return render(request, 'Onto_Manipulation/download.html', {})


def download_XLS(request):
    working_ontology = get_working_ontology()
    Onto_mapping.create_xls(working_ontology)
    Onto_mapping.create_zip()
    pwd = os.path.dirname(__file__)
    file_path = os.path.join(pwd, 'data/ontology.zip')

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
        filename = os.path.join(pwd, 'data/ontology_edited.xml')
        xml_target = open(filename, 'wb')
        ontology = xmltodict.parse(request.FILES['xmlfile'])
        xmltodict.unparse(ontology, output=xml_target)


    return render(request, 'Onto_Manipulation/convert.html', {'list':Onto_mapping.list_ontologies()})

def upload_XLS(request):
    if request.method == 'POST' and request.FILES:
        if request.FILES['xlsrelation']:
            rel = request.FILES['xlsrelation']
            cat = request.FILES['xlscategory']
            pwd = os.path.dirname(__file__)
            filerel = os.path.join(pwd, 'data/relations.xls')
            filecat = os.path.join(pwd, 'data/categories.xls')
            if(not os.path.exists(filerel)):
                os.makedirs(filerel)
            if (not os.path.exists(filecat)):
                os.makedirs(filecat)
            with open(filerel, 'wb+') as destination:
                for chunk in rel.chunks():
                    destination.write(chunk)

            with open(filecat, 'wb+') as destination:
                for chunk in cat.chunks():
                    destination.write(chunk)
            out_file = 'ontology.xml'

            # this part makes sure that the application won't override a pre-existent ontology
            counter = 0
            while(os.path.exists(os.path.join(pwd, 'data/', out_file))):
                counter += 1
                out_file = out_file.split('.')
                out_file = out_file[0].split('_')
                out_file = out_file[0] + '_' + str(counter) + '.xml'
            print(os.path.join('data/', out_file))
            Onto_mapping.create_xml('relations.xls', 'categories.xls', out_file)
            out_file = out_file.split('.')

    return redirect('/edit/'+out_file[0])
    #return render(request, 'Onto_Manipulation/edit.html', {'list':Onto_mapping.list_ontologies()})

def select(request, id=""):
    if (id == 'default'):
        set_working_ontology('ontology.xml')
    else:
       set_working_ontology(id+'.xml')

    return redirect('/relation', dict)

# Create your views here.
