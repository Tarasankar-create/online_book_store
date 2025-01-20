from django.shortcuts import render

def pub_register(request):
    return render(request,'publisher_register.html')

def cus_home(request):
    cname=request.session.get('name')
    return render(request,'cus_home.html',{'cus_name':cname})