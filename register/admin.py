from django.contrib import admin
from .models import pub_register
from .models import cus_register
# Register your models here.
admin.site.register(pub_register)
admin.site.register(cus_register)