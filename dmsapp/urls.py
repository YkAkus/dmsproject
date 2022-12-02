from django.urls import path
from dmsapp import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(views.FileUploader.as_view()),name='index'),
    path('files/', views.allFile, name="file-view"),
    path('favourite/', views.favFileView, name="fav-file-view"),
    path('del-files/', views.deleteFile, name="del-file"),
    path('remove-files/', views.removeFile, name="remove-file"),
    path('make-fav/', views.makeFav, name="fav-file"),
    path('restore-file/', views.restoreFile, name="restore-file"),
    path('trash/', views.remFileView, name="trash"),
    path("auth",views.auth,name="auth"),
    path("folder/<str:name>/",views.openFolder,name="folder-data"),
]