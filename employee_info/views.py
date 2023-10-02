from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context = {}
   
       
    classes = models.Information.objects.all().order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'home.html',context)

def genneral(request):
    context = {}
   
       
    classes = models.Information.objects.filter(class_Department=1).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'purchasing.html',context)

def special_subjects(request):
    context = {}
   
       
    classes = models.Information.objects.filter(class_Department=2).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'providing.html',context)

def elective_subjects(request):
    context = {}
   
       
    classes = models.Information.objects.filter(class_Department=3).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'aftersale.html',context)

def search(request):
    context = {}
   
       
    classes = models.Information.objects.filter(class_category=3).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'elective_subjects.html',context)

def about(request):
    context = {}
   
       
    classes = models.Classes.objects.all().order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'about.html',context)

