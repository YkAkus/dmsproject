from django.contrib import admin
from django.contrib.auth import models
from dmsapp.models import File, Folder,Profile,Fileview


# Register your models here.
admin.site.register(File)
admin.site.register(Folder)
admin.site.register(Profile)
admin.site.register(Fileview)