from django.urls import path
from dmsapp import views

urlpatterns = [
    path('', views.index,name='index'),
]