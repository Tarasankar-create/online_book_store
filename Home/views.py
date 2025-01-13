from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import contact_master

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('coname')
        email=request.POST.get('coemail')
        mobile=request.POST.get('cocontact')
        address=request.POST.get('coaddress')
        ob=contact_master.objects.create(coname=name,coemail=email,cocontact=mobile,coaddress=address)
        ob.save()
        return render(request,'contact.html',{'msg':'Register successfully'})
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def index(request):
    return HttpResponse("<h1>Online book store</h1>")