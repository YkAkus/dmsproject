from allauth.account.forms import SignupForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from requests import request
from .forms import FileForm, FolderForm, FolderFileForm
from django.contrib.auth.models import User, Group
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import File, Folder, FolderFile ,Profile ,Fileview
from .sftp_handler import test,createfol,upfile, delfile, delfolder
import urllib


def redirect_params(url, params=None):
    response = redirect(url)
    if params:
        query_string = urllib.parse.urlencode(params)
        response['Location'] += '?' + query_string.replace("%20", " ")
    return response

class FileUploader(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        r = False
        if request.user.is_superuser:
            r = True
        arg = request.GET.get("folder", None)
        obj = File.objects.filter(user = request.user, is_delete=False)
        if arg:
            sffo,sffi = test(request.user.username,r, arg)
        else:
            sffo,sffi = test(request.user.username, r)
        # print(sffi,sffo)


        pho = Profile.objects.filter(user = request.user)
        folder = Folder.objects.filter(user = request.user,is_delete=False)
        form = FileForm()
        folderForm = FolderForm()
        group = Group.objects.get(name="client")
        permission = group.permissions.all()
        groups=Group.objects.all()
        
        return render(request, 'index.html', {'form':form,'folderform':folderForm, 'files':obj, 'folders':folder,"pho":pho, "permissions":permission,'groups':groups, 'sdir':sffo,'sfile':sffi})
    def post(self, request):
        arg = request.POST.get("curUrl", None)
        if arg == "/":
            arg = False
        if not request.user.is_authenticated:
            return JsonResponse({"data":"Method Not Allowed Here"})
        r = False
        if request.user.is_superuser:
            r = True
        if request.POST.get("form_type") == "folderfrm":
            form = FolderForm(request.POST)
            if form.is_valid():
                name = request.POST.get("name",None)
                frm = form.save(commit=False)
                frm.user = request.user
                frm.save()
                if arg:
                    createfol(request.user,name,r, arg.split("?folder=")[1])
                else:
                    createfol(request.user,name, r)
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
                else:
                    ext = ""
                    ext = frm.file.name
                    frm.name = ext
                    frm.file.name = ext
                    frm.save()
            else:
                ext = ""
                # fil=request.FILES.getlist("file")
                ext=frm.file.name
                frm.name = ext
                frm.file.name = ext
                frm.save()
            if arg:
                upfile(request.user.username,"."+frm.file.url,r, arg.split("?folder=")[1])
            else:
                upfile(request.user.username,"."+frm.file.url,r)
            return JsonResponse({'status':True,'data':'File uploaded'})
        else:
            return JsonResponse({'status':False,'data':'Something went wrong!!'})

# D:\dmsproject\media\uploads\files\A.pdf
def auth(request):
    tfile = File.objects.filter( is_delete=False).count()
    tfolder = Folder.objects.filter(is_delete=False).count()
    tuser=User.objects.all().count()
    tshaer=Fileview.objects.all().count()
    shear=Fileview.objects.all()
    pho=Profile.objects.filter(user = request.user)
    groups=Group.objects.all()
    alluser=User.objects.all()
    group = request.POST.get('group')
    user = request.POST.get('user')
    if request.method == "POST":
        if request.POST.get("form_type") == 'profile':
            u=User.objects.get(username=request.user)
            u.first_name=request.POST.get("firstName",None)
            u.last_name=request.POST.get("lastName",None)
            try:
                obj= Profile.objects.get(user=request.user)
            except:
                obj= Profile.objects.create(user=request.user)
            obj.mobile=request.POST.get("mobile",None)
            img=request.FILES.getlist("uploading")
            for i in img:
                obj.img=i
            obj.save()
            if u!=request.user:
                u.save()
            try:
                obj= Profile.objects.get(user=request.user)
            except:
                obj= Profile.objects.create(user=request.user)
        elif request.POST.get("form_type") == 'perm':
            User.objects.get(id = user).groups.clear()
            get_group = Group.objects.get(name=group)
            get_group.user_set.add(user)
    return render(request,"auth.html",{"pho":pho,"groups":groups,"alluser":alluser,'tfile':tfile,'tfolder':tfolder,'tuser':tuser,'tshaer':tshaer,'shear':shear})


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
    obj = File.objects.filter(user = request.user, is_delete=False)
    return render(request, "allfiles.html", {'files':obj, 'form':form})


@login_required
def viewFile(request, url):
    user = request.user
    file = get_object_or_404(File, url = url, is_delete=False)
    myfileview = Fileview()
    myfileview.user = file.user
    myfileview.open_by = user
    myfileview.shear_file = file
    myfileview.opened_when = datetime.now()
    myfileview.times_open = 1
    myfileview.save()
    return render(request, "file.html", {"file":file})


@login_required
def FileView(request):
    files = File.objects.filter(user = request.user, is_delete=False)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfiles.html", context)


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
    arg = request.POST.get("url", None)
    print(id, arg)
    if arg == "/":
        arg = False

    r = False
    if request.user.is_superuser:
        r = True
    if arg:
        delfile(request.user,r,id, arg.split("?folder=")[1])
    else:
        delfile(request.user, r, id)
    return JsonResponse({'status':True,'data':'File uploaded'})
@login_required
def removeFolder(request):
    id = request.POST.get("id", False)
    arg = request.POST.get("url", None)
    if arg == "/":
        arg = False

    r = False
    if request.user.is_superuser:
        r = True
    if arg:
        delfolder(request.user,r, id,arg.split("?folder=")[1])
    else:
        delfolder(request.user, r, id)
    return JsonResponse({'status':True,'data':'File uploaded'})

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
@login_required
def search(request):
    pho=Profile.objects.filter(user = request.user)
    if request.method=="POST":
        searched=request.POST['searched']
        serfol= Folder.objects.filter(user = request.user, is_delete=False,name__contains=searched)
        serfil=File.objects.filter(user = request.user, is_delete=False,name__contains=searched)
        return render(request,"search.html",{'searched':searched,'serfol':serfol,"serfil":serfil,'pho':pho})
    else:
        return render(request,"search.html")
def fifo_auth(request):
    
    return render