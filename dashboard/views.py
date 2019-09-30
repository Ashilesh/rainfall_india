from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Index
from . import helper

# Create your views here.

# practice
def index(request):
    index = Index()

    arr1 =  ['January', 'February', 'March', 'April', 'May','June','July','August','September','Octomber','November','December']
    return render(request,'index.html',{'index' : index,'arr1' : arr1})

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


def ajax_chart(request):
    year = request.GET.get('year', None)

    list_get = helper.get_chart(year)

    min_rainfall_value = min(list_get[1:13])
    min_rainfall_index = list_get.index(min(list_get[1:13]))
    min_rainfall_month = helper.get_month(min_rainfall_index)

    max_rainfall_value = max(list_get[1:13])
    max_rainfall_index = list_get.index(max(list_get[1:13]))
    max_rainfall_month = helper.get_month(max_rainfall_index)

    data = {
        'year' : year,
        'x' : list_get[1:13],
        'annual' : list_get[13],
        'min_rainfall_value' : min_rainfall_value,
        'min_rainfall_month' : min_rainfall_month,
        'max_rainfall_value' : max_rainfall_value,
        'max_rainfall_month' : max_rainfall_month
    }

    return JsonResponse(data)
