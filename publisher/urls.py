from django.urls import path
from publisher import views as pviews
urlpatterns=[
    path('pub_home',pviews.pub_home,name='pubhome'),
    path('add_book',pviews.add_book,name='addbook'),
]