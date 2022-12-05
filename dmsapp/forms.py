from dataclasses import fields
from django.forms import ModelForm,forms
from .models import File, Folder, FolderFile,Profile
from django.contrib.auth.models import User
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['title','desc','file']

class FolderFileForm(ModelForm):
    class Meta:
        model = FolderFile
        fields = ['folder','title','desc','file']

class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('img', 'mobile')
 
 
