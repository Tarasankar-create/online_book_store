from django.urls import path
from register import views
urlpatterns=[
    path('pubregister',views.publisher_register,name='pubregister'),
    path('cusregister',views.customer_register,name='cusregister')
]