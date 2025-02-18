from django.urls import path
from . import views as views
urlpatterns=[
    path('cus_home',views.cus_home,name='cushome'),
    path('customer/bookcatagory',views.bookcatagory,name='bookcatagory'),
    
]