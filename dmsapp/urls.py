from django.urls import path
from dmsapp import views, views_perm
from django.contrib.auth.decorators import login_required
from .views_perm import GP

urlpatterns = [
    path('', login_required(views.FileUploader.as_view()),name='index'),
    path('files/', views.allFile, name="file-view"),
    path('favourite/', views.favFileView, name="fav-file-view"),
    # path('del-files/', views.deleteFile, name="del-file"),
    # path('del-folder/', views.deleteFolder, name="del-folder"),
    path('remove-files/', views.removeFile, name="remove-file"),
    path('remove-folders/', views.removeFolder, name="remove-folders"),
    path('make-fav/', views.makeFav, name="fav-file"),
    path('restore-file/', views.restoreFile, name="restore-file"),
    path('trash/', views.remFileView, name="trash"),
    path("auth",views.auth,name="auth"),
    path("search",views.search,name="search"),
    path("folder/<str:name>/",views.openFolder,name="folder-data"),
    path("all/perm/",views_perm.allperm,name="allperm"),
    path("perm/",login_required(GP.as_view()),name="perm"),
]