from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello),
    path('dispaly_date/', views.dispaly_date),
    path('menu/', views.menu),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    path('getuser/', views.queryview, name='queryview'), 
    path('showform/', views.showform, name='showform'), 
    path('getform/', views.getform , name='getform'), 
    path('menu/<int:menu_id>', views.menu_by_id, name = 'menu_by_id'),
]