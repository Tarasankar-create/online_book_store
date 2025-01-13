from django.shortcuts import render

def pub_register(request):
    return render(request,'publisher_register.html')
