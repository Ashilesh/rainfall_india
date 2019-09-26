from django.shortcuts import render
from django.http import HttpResponse
from .models import Index

# Create your views here.

# practice
def index(request):
    index = Index()
    arr = [0, 2, 6.7, 3, 5.6, 240, 220.5, 300.4, 170.5, 112, 3, 3.7]
    arr1 =  ['January', 'February', 'March', 'April', 'May','June','July','August','September','Octomber','November','December']
    return render(request,'index.html',{'index' : index,'arr': arr, 'arr1' : arr1})

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
