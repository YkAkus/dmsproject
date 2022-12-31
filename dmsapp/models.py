import re
from django.db import models
from django.contrib.auth.models import User
from .utils import create_shortened_url
from django.dispatch import receiver
from django.db.models.signals import post_save



FTP_HOST = "216.48.189.99"
FTP_USER = "root"
FTP_PASS = "NHYKXN@sxpkc988"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    import pysftp as sftp
    if created:
        cnopts = sftp.CnOpts()  
        cnopts.hostkeys = None
        with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ... ")
            sftp.cwd('/JnP/')
            sftp.mkdir(instance.username, mode=777)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.FileField(upload_to='user/',blank=True,null=True)
    mobile = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='New_Folder', unique=True)
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
    name = models.CharField(max_length=100)
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

class Fileview(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True,blank=True)
    open_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    shear_file = models.ForeignKey(File,on_delete=models.CASCADE, null=True,blank=True)
    opened_when= models.DateTimeField(auto_now_add=True, blank=True,null=True,)
    times_open= models.CharField(max_length=30,blank=True,null=True,) 
    def __str__(self):
        return  "%s"  %  (self.shear_file)
