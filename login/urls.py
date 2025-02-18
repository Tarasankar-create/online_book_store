from django.urls import path
from login import views as lviews
from customer import views as cuviews
urlpatterns=[
    path('pub_login',lviews.pub_login,name='publogin'),
    path('cus_login',lviews.cus_login,name='cuslogin'),
    path('cus_home',cuviews.cus_home,name='cus_home'),
]