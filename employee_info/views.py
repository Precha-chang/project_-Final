from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context = {}
   
       
    classes = models.Information.objects.all().order_by("fname")
   
    context["employees"] = classes

 
   
    return render(request, 'home.html',context)


def purchasing(request):
    context = {}
   
       
    classes = models.Information.objects.filter(department=1).order_by("id")
   
    context ["employees"] = classes
 
   
    return render(request, 'purchasing.html',context)
def providing(request):
    context = {}
   
       
    classes = models.Information.objects.filter(department=2).order_by("id")
   
    context ["employees"] = classes
 
   
    return render(request, 'providing.html',context)



def aftersale(request):
    context = {}
   
       
    classes = models.Information.objects.filter(department=3).order_by("id")
   
    context ["employees"] = classes
 
   
    return render(request, 'aftersale.html',context)


# def search(request):
#     context = {}
   
       
#     classes = models.Information.objects.filter(class_category=3).order_by("id")
   
#     context ['classes'] = classes
 
   
#     return render(request, 'elective_subjects.html',context)

def about(request):
    context = {}
   
       
    classes = models.Information.objects.all().order_by("fname")
   
    context ["employees"] = classes
 
   
    return render(request, 'about.html',context)

