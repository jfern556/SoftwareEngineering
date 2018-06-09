from django.urls import path
from . import views

from django.views.generic import TemplateView
#book
#from django.conf.urls.defaults import *




#^notice django.urls import path, not django.urls import url

urlpatterns = [
    path('', views.index, name='index'),         
    path('myCart/', views.myCart, name="myCart"),
    #path("example/", TemplateView.as_view(template_name = 'myCart/example.html')),
    path('example/', views.example, name="example"),

    #testing
    path('session/', views.consoleSessionDisplay, name="session")
]