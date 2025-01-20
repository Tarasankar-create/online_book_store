from django.urls import path
from login import views as lviews
urlpatterns=[
    path('pub_login',lviews.pub_login,name='publogin'),
    path('cus_login',lviews.cus_login,name='cuslogin'),
]