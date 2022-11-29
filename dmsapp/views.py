from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import FileForm
from django.views import View
from django.http import JsonResponse
from .models import File
class FileUploader(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        obj = File.objects.filter(user = request.user)
        form = FileForm()
        return render(request, 'index.html', {'form': form, 'files':obj})

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"data":"Method Not Allowed Here"})
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