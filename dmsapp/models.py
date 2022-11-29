from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/files/', max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=15, unique=True, blank=True)
    is_delete = models.BooleanField(default=False)
    is_fav = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
