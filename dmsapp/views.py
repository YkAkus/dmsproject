from allauth.account.forms import SignupForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from requests import request
from .forms import FileForm, FolderForm, FolderFileForm
from django.contrib.auth.models import User, Group
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import File, Folder, FolderFile,Profile


class FileUploader(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        obj = File.objects.filter( is_delete=False)
        pho = Profile.objects.filter(user = request.user)
        folder = Folder.objects.filter( is_delete=False)
        form = FileForm()
        folderForm = FolderForm()
        group = Group.objects.get(name="admin")
        permission = group.permissions.all()
        return render(request, 'index.html', {'form': form,'folderform':folderForm, 'files':obj, 'folders':folder,
                                            "pho":pho, "permissions":permission,})

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
                return JsonResponse({'status':True,'data':'Folder Created'})
            else:
                return JsonResponse({'status':False,'data':'Folder with same name already exists'})
        form = FileForm(request.POST, request.FILES)
        check=request.POST.get("coupon_question",None)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user = request.user
            if check == "1":
                name = request.POST.get("name",None)
                if name:
                    ext = ""
                    if "." in frm.file.url:
                        ext = "."+frm.file.url.split(".")[-1]
                    frm.file.name = name+ext
                    frm.save()
                    return JsonResponse({'status':True,'data':'File uploaded'})
                else:
                    ext = ""
                    ext = frm.file.name
                    frm.name = ext
                    frm.file.name = ext
                    frm.save()
                    return JsonResponse({'status':True,'data':'File uploaded'})
            else:
                ext = ""
                ext = frm.file.name
                frm.name = ext
                frm.file.name = ext
                frm.save()
                return JsonResponse({'status':True,'data':'File uploaded'})
        else:
            return JsonResponse({'status':False,'data':'Something went wrong!!'})
def auth(request):
        
        # for i in User.objects.get(id = user).groups.all():
        #     get_group = Group.objects.get(name=i)
        #     user.groups.remove()
    pho=Profile.objects.filter(user = request.user)
    groups=Group.objects.all()
    alluser=User.objects.all()
    if request.method == "POST":
        u=User.objects.get(username=request.user)
        u.first_name=request.POST.get("firstName",None)
        u.last_name=request.POST.get("lastName",None)
        u.save()
        try:
            obj= Profile.objects.get(user=request.user)
        except:
            obj= Profile.objects.create(user=request.user)
        obj.mobile=request.POST.get("mobile",None)
        img=request.FILES.getlist("uploadimg")
        for i in img:
            obj.img=i
        obj.save()
        group = request.POST.get('group')
        user = request.POST.get('user')
        if group and user != None:
            User.objects.get(id = user).groups.clear()
            get_group = Group.objects.get(name=group)
            get_group.user_set.add(user)
        return redirect("/auth",{"pho":pho})
    try:
        obj= Profile.objects.get(user=request.user)
    except:
        obj= Profile.objects.create(user=request.user)
    return render(request,"auth.html",{"pho":pho,"groups":groups,"alluser":alluser})

def openFolder(request, name):
    pho=Profile.objects.filter(user = request.user)
    if request.method == "POST":
        form = FolderFileForm(request.POST, request.FILES)
        folder = request.POST.get("folder",None)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user = request.user
            ext = ""
            ext = frm.file.name
            frm.name = ext
            frm.file.name = ext
            frm.save()
            return JsonResponse({'status':True,'data':'Data uploaded'})
        else:
            return JsonResponse({'status':False,'data':'Something went wrong!!'})
    obj = FolderFile.objects.filter(folder = Folder.objects.get(name = name),is_delete = False)
    form = FolderFileForm()
    return render(request, "folderfiles.html", {'files':obj, 'form':form, 'folder':Folder.objects.get(name = name).id,'name':name,'pho':pho})
    
def allFile(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user = request.user
            ext = ""
            ext = frm.file.name
            frm.name = ext
            frm.file.name = ext
            frm.save()
            return JsonResponse({'status':True,'data':'File uploaded'})
        else:
            return JsonResponse({'status':False,'data':'Something went wrong!!'})
    form = FileForm()
    obj = File.objects.filter( is_delete=False)
    return render(request, "allfiles.html", {'files':obj, 'form':form})

def viewFile(request, url):
    file = get_object_or_404(File,url = url, is_delete=False)
    return render(request, "file.html", {"file":file})

@login_required
def FileView(request):
    files = File.objects.filter( is_delete=False)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfiles.html", context)


@login_required
def favFileView(request):
    files = File.objects.filter( is_delete=False, is_fav=True)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfavfiles.html", context)

@login_required
def remFileView(request):
    files = File.objects.filter( is_delete=True)
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
def removeFolder(request):
    fid = request.POST["id", False]
    fol = Folder.objects.get(id = id)
    fol.is_delete = True
    fol.save()
    return JsonResponse({"data":True})

@login_required
def deleteFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.delete()
    return JsonResponse({"data":True})
@login_required
def deleteFolder(request):
    id = request.POST["id"]
    folder = Folder.objects.get(id = id)
    folder.delete()
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
def search(request):
    pho=Profile.objects.filter(user = request.user)
    if request.method=="POST":
        searched=request.POST['searched']
        serfol= Folder.objects.filter(name__contains=searched)
        serfil=File.objects.filter(name__contains=searched)
        return render(request,"search.html",{'searched':searched,'serfol':serfol,"serfil":serfil,'pho':pho})
    else:
        return render(request,"search.html")