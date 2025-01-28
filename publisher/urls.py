from django.urls import path
from publisher import views as pviews
urlpatterns=[
    path('pub_home',pviews.pub_home,name='pubhome'),
    path('addbook',pviews.addbook,name='addbook'),
    path('viewbook',pviews.viewbook,name='viewbook'),
]