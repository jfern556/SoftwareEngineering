from django.urls import path
from . import views

app_name = "BookDetails"
urlpatterns = [
	path('', views.index, name ='index'),
	path('working/', views.working, name=''),
	path('notworking/', views.notworking, name=''),
]


