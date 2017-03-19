from django.shortcuts import render
from Onto_Manipulation import Onto_mapping
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

def edit_cat(request):
    if request.method == 'POST':
        categoryName = request.POST['name']
        englishName = request.POST['english']
        humanFormat = request.POST['human']
        # visibleTrue = request.POST['options1']
        # visibleFalse = request.POST['options2']
        generalization = request.POST['generalization']
        mutexException = request.POST['mutex']
        knowNegatives = request.POST['negatives']
        seedInstaves = request.POST['instances']
        seedPatterns = request.POST['patterns']
        conceptSynonyms = request.POST['synonyms']
        author = request.POST['author']
        description = request.POST['desc']
        comment = request.POST['comment']

        pwd = os.path.dirname(__file__)
        xml_path = os.path.join(pwd, 'static/Onto_Manipulation/data/ontology.xml')
        xml = etree.parse(xml_path)
        root = etree.Element('Ontology')
        cats = etree.SubElement(root, 'Categories')
        cat = etree.SubElement(cats, 'Category')
        cat.set('id',"999")


        test = etree.SubElement(cat, 'categoryName')
        test.text = (str(categoryName)).encode('utf8')
        test = etree.SubElement(cat, 'englishName')
        test.text = (str(englishName)).encode('utf8')
        test = etree.SubElement(cat, 'humanFormat')
        test.text = (str(humanFormat)).encode('utf8')

        xml.write('static/Onto_Manipulation/data/ontology.xml')


    return render(request, 'Onto_Manipulation/edit_cat.html', {})

def edit_rel(request):
    return render(request, 'Onto_Manipulation/edit_rel.html', {})

def convert(request):
    return render(request, 'Onto_Manipulation/convert.html',{})

def download(request):
    return render(request, 'Onto_Manipulation/download.html', {})


# Create your views here.
