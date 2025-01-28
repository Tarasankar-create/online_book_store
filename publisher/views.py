from django.shortcuts import render,redirect
from.models import Catagory,Add_Book

def pub_home(request):
    name=request.session.get('pname')
    return render(request,'pub_home.html',{'name':name})
def addbook(request):
    ob=Catagory.objects.all()
    if request.method=='POST':
        cname=request.POST['cname']
        catagory_name=Catagory.objects.get(c_name=cname)
        bname=request.POST['bname']
        aname=request.POST['aname']
        isbnno=request.POST['isbn']
        bprice=request.POST['bprice']
        dis=request.POST['dis']
        image=request.FILES['bimage']
        obj=Add_Book.objects.create(c_name=catagory_name,book_name=bname,authorname=aname,isbn=isbnno,price=bprice,discount=dis,bookdoc=image)
        ob.save()
        return redirect('addbook')
    return render(request,'add_book.html')
def viewbook(request):
    ob=Add_Book.objects.all()
    return render(request,'viewbook.html',{'bookdata':ob})