from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from requests import request
from .forms import FileForm, FolderForm, FolderFileForm
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import File, Folder, FolderFile
class FileUploader(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        obj = File.objects.filter(user = request.user, is_delete=False)
        folder = Folder.objects.filter(user = request.user, is_delete=False)
        form = FileForm()
        folderForm = FolderForm()
        return render(request, 'index.html', {'form': form,'folderform':folderForm, 'files':obj, 'folders':folder})

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"data":"Method Not Allowed Here"})
        if request.POST.get("form_type") == "folderfrm":
            form = FolderForm(request.POST)
            # name = request.POST.get("name", None)
            if form.is_valid():
                frm = form.save(commit=False)
                frm.user = request.user
                frm.save()
                return JsonResponse({'data':'Data uploaded'})
            else:
                return JsonResponse({'data':'Something went wrong!!'})
        
        form = FileForm(request.POST, request.FILES)
        title = request.POST.get("title",None)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user = request.user
            if title:
                ext = ""
                if "." in frm.file.url:
                    ext = "."+frm.file.url.split(".")[-1]
                frm.file.name = title+ext
            frm.save()
            return JsonResponse({'data':'Data uploaded'})
        else:
            return JsonResponse({'data':'Something went wrong!!'})

def openFolder(request, name):
    if request.method == "POST":
        form = FolderFileForm(request.POST, request.FILES)
        title = request.POST.get("title",None)
        folder = request.POST.get("folder",None)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.folder = Folder.objects.get(id = folder)
            if title:
                ext = ""
                if "." in frm.file.url:
                    ext = "."+frm.file.url.split(".")[-1]
                frm.file.name = title+ext
            frm.save()
            return JsonResponse({'data':'Data uploaded'})
        else:
            return JsonResponse({'data':'Something went wrong!!'})
    obj = FolderFile.objects.filter(folder = Folder.objects.get(name = name),is_delete = False)
    form = FolderFileForm()

    return render(request, "folderfiles.html", {'files':obj, 'form':form, 'folder':Folder.objects.get(name = name).id, 'name':name})

    
def allFile(request):
    obj = File.objects.filter(user = request.user, is_delete=False)
    return render(request, "allfiles.html", {'files':obj})

def viewFile(request, url):
    file = get_object_or_404(File,url = url, is_delete=False)
    return render(request, "file.html", {"file":file})

@login_required
def FileView(request):
    files = File.objects.filter(user = request.user, is_delete=False)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfiles.html", context)

@login_required
def auth(request):
    return render(request, "authority.html")


@login_required
def favFileView(request):
    files = File.objects.filter(user = request.user, is_delete=False, is_fav=True)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfavfiles.html", context)

@login_required
def remFileView(request):
    files = File.objects.filter(user = request.user, is_delete=True)
    context = {
        "files" : files
    }
    return render(request, "trash.html", context)

@login_required
def removeFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.is_delete = True
    file.save()
    return JsonResponse({"data":True})

@login_required
def deleteFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.delete()
    return JsonResponse({"data":True})

@login_required
def restoreFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.is_delete = False
    file.is_fav = False
    file.save()
    return JsonResponse({"data":True})

@login_required
def makeFav(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    if file.is_fav:
        file.is_fav = False
    else:
        file.is_fav = True
    file.save()
    return JsonResponse({"data":file.is_fav})