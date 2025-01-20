from django.shortcuts import render

def pub_home(request):
    name=request.session.get('pname')
    return render(request,'pub_home.html',{'name':name})
def add_book(request):
    return render(request,'add_book.html',)
