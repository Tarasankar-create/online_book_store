from django.db import models

# Create your models here.
class contact_master(models.Model):
    coname=models.CharField(max_length=50)
    cocontact=models.CharField(max_length=50)
    coemail=models.CharField(max_length=50)
    coaddress=models.CharField(max_length=100)