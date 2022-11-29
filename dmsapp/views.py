from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FileForm
@login_required
def index(request):
    frm = FileForm()
    if request.method == "POST":
        pass
    return render(request,'index.html', {'form':frm})