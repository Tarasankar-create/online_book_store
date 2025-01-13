from django.shortcuts import render
from .models import cus_register,pub_register

def publisher_register(request):
    if request.method=='POST':
        name=request.POST.get('pname')
        email=request.POST.get('pemail')
        mobile=request.POST.get('pmobno')
        pwd=request.POST.get('ppwd')
        doc=request.POST.get('pdoc')
        address=request.POST.get('paddress')
        ob=pub_register.objects.create(pname=name,pemail=email,pmobileno=mobile,ppwd=pwd,pdoc=doc,paddress=address)
        ob.save()
        return render(request,'publisher_register.html',{'msg':'Register success'})

    return render(request,'publisher_register.html')
 
def customer_register(request):
    if request.method=='POST':
        name=request.POST.get('cname')
        email=request.POST.get('cemail')
        mobile=request.POST.get('ccontact')
        pwd=request.POST.get('cpwd')
        dob=request.POST.get('cdob')
        address=request.POST.get('caddress')
        ob=cus_register(cname=name,cemail=email,ccontact=mobile,cpwd=pwd,cdob=dob,caddress=address)
        ob.save()
        return render(request,'customer_register.html',{'msg':'Register success'})
    return render(request,'customer_register.html')
