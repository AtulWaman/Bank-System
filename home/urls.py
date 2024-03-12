from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
    path("",views.index,name='home') ,
    path("about",views.about,name='about') ,
    path("services",views.services,name='services') ,
    path("contact",views.contact,name='contact') ,
    path("allcustomers",views.allcustomers,name='allcustomers') ,
    path("perticular_cust",views.perticular_cust,name='perticular_cust'),
    # path("trans",views.trans,name='trans'),
    path("transfer_money",views.transfer_money,name='transfer_money')
]