from django.shortcuts import render,redirect    
from register.models import pub_register,cus_register
# Create your views here.
def pub_login(request):
        if request.method=='POST':
            email=request.POST['pemail']
            password=request.POST['ppwd']
            try:
                ob=pub_register.objects.get(pemail=email,ppwd=password)
                request.session['pname']=ob.pname
                request.session['pemail']=ob.pemail
                if ob.status==1:
                    return redirect('pub_home')
                else:
                    return render(request,'pub_login.html',{'msg':'Waiting for admin conformation'})
            except Exception as e:
                return render(request,'pub_login.html',{'msg':'Invalid' +str(e)})
        return render(request,'pub_login.html')

def cus_login(request):
        if request.method=='POST':
            email=request.POST['cemail']
            password=request.POST['cpwd']
            try:
                ob=cus_register.objects.get(cemail=email,cpwd=password)
                request.session['cname']=ob.cname
                request.session['cemail']=ob.cemail
                if ob.status==1:
                    return redirect('cus_home')
                else:
                    return render(request,'cus_login.html',{'msg':'Waiting for admin conformation'})
            except Exception as e:
                return render(request,'cus_login.html',{'msg':'Invalid' +str(e)})
        return render(request,'cus_login.html')