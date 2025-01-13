from django.db import models
from django.utils import timezone

# Create your models here.
class pub_register(models.Model):
    pname=models.CharField(max_length=50)
    pemail=models.CharField(primary_key=True,max_length=50)
    pmobileno=models.CharField(max_length=50)
    ppwd=models.CharField(max_length=30)
    date=models.DateField(default=timezone.now)
    pdoc=models.FileField(upload_to='document/')
    paddress=models.CharField(max_length=100)
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.pname

class cus_register(models.Model):
    cname=models.CharField(max_length=50)
    ccontact=models.CharField(max_length=50)
    cemail=models.CharField(primary_key=True,max_length=50)
    cpwd=models.CharField(max_length=30)
    cdob=models.CharField(max_length=30)
    caddress=models.CharField(max_length=100)
    def __str__(self):
        return self.cname