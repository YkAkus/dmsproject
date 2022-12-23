from django.contrib.auth.models import Group, Permission, User
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from .models import File, Folder, FolderFile
from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def allperm(request):
    if request.method == 'POST':      
        all_p = []
        models = [File, Folder, FolderFile]      
        for model in models:      
            content_type = ContentType.objects.get_for_model(model)
            post_permission = Permission.objects.filter(content_type=content_type)
            all_p += ["dashboard."+perm.codename for perm in post_permission]
        user_name = request.POST.get('user')
        a=Group.objects.get(name=user_name)
        a_all=a.permissions.all()
        return JsonResponse({"a_all":list(a_all.values()), "all_p":all_p})

class GP(View):
    def get(self,request):
        try:
            all_group=Group.objects.all()
            return render(request,'groups.html',{"all_group":all_group})
        except Exception as e:
            path = request.path
            return render(request, "groups.html",{"exceptionRaise":"exceptionRaise","Curpath":path,"errTitle":"Page can't be opened",'errOutput':str(e)})

    def post(self, request):
        try:
            all_group=Group.objects.all()
            data = {key:request.POST[key].strip() for key in request.POST if not key == "csrfmiddlewaretoken"}
            all_change = []
            p = request.POST.getlist('permission')
            string_search = "dashboard.add_"
            all_add = [x for x in p if x.startswith(string_search)]
            all_change += [x.replace('.add_', '.change_') for x in all_add]
            p = all_change + p
                
            group_django = Group.objects.get(name=data['groupname'])
            perm_set = Permission.objects.values("codename","id")
            perm_ids = []
            for i in perm_set:
                for perm in p:
                    if perm.split(".")[1] in i["codename"]:
                        perm_ids.append(i["id"])
                
            group_django.permissions.set(perm_ids)
            return render(request,'groups.html',{"all_group":all_group,'msg':'Permissions Set'})
        except Exception as e:
            pass
def user_per(request):
    
    return JsonResponse()