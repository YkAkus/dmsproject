from django.contrib import admin
from django.contrib.auth import models
from dmsapp.models import File, Folder


# Register your models here.
admin.site.register(File)
admin.site.register(Folder)