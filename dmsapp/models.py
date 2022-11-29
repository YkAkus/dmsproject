from django.db import models

# Create your models here.
class registers(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.email
    class Mata:
        managed = True
