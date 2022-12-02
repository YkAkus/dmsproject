from dataclasses import fields
from django.forms import ModelForm
from .models import File, Folder, FolderFile
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