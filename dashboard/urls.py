from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name ='index'),
    path('chart',views.chart, name = 'chart'),
    path('map', views.map, name = 'map'),
    path('table', views.table, name = 'table'),
    path('about_us', views.about_us, name = 'about_us'),
    path('vision', views.vision, name = 'vision')
]
