import re
from django.db import models
from django.contrib.auth.models import User
from .utils import create_shortened_url

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.FileField(upload_to='user/',blank=True,null=True)
    mobile = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='New Folder', unique=True)
    date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    is_fav = models.BooleanField(default=False)

    def totalFolder(self):
        obj = FolderFile.objects.filter(folder = self, is_delete = False).count()
        return obj

    def __str__(self):
        return self.name
class FolderFile(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/files/', max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/files/', max_length=100)
    name = models.CharField(max_length=100, null=True)
    desc = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=15, unique=True, blank=True)
    is_delete = models.BooleanField(default=False)
    is_fav = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = create_shortened_url(self)
        super().save(*args, **kwargs)
