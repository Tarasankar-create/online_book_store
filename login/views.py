from django.shortcuts import render,redirect
from register.models import pub_register
# Create your views here.
def pub_login(request):
        if request.method=='POST':
            email=request.POST['pemail']
            password=request.POST['ppwd']
            try:
                ob=pub_register.objects.get(pemail=email,ppwd=password)
                return render(request,'pub_home.html')
            except:
                return render(request,'pub_login.html',{'msg':'Invalid email or password'})
        return render(request,'pub_login.html')