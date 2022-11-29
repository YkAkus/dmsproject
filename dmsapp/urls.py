from django.urls import path
from dmsapp import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(views.FileUploader.as_view()),name='index'),
]