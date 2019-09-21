from django.shortcuts import render
from django.http import HttpResponse
from .models import Index

# Create your views here.

# practice
def index(request):
    index = Index()
    return render(request,'index.html',{'index' : index})

def chart(request):
    return render(request, 'chart.html')

def map(request):
    return render(request, 'map.html')

def table(request):
    return render(request, 'table.html')

def about_us(request):
    return render(request, 'about_us.html')

def vision(request):
    return render(request, 'vision.html')
