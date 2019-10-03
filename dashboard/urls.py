from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name ='index'),
    path('chart',views.chart, name = 'chart'),
    path('map', views.map, name = 'map'),
    path('table', views.table, name = 'table'),
    path('about_us', views.about_us, name = 'about_us'),
    path('vision', views.vision, name = 'vision'),
    path('ajax/chart',views.ajax_chart, name = 'ajax_chart'),
    path('ajax/map',views.ajax_map, name = 'ajax_map')
]
