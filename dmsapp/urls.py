from django.urls import path
from dmsapp import views

urlpatterns = [
    path('', views.login,name='login'),
    path('forgot', views.forgot,name='forgot'),
    path('createlog', views.createlog,name='createlog'),
    path('reg',views.reg,name='reg'),
    path('index', views.index,name='index'),
    path('table', views.table,name='table'),
    path('chart', views.chart,name='chart'),
]