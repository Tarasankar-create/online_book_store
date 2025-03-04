from django.urls import path
from . import views as cviews
urlpatterns=[
    path('cus_home',cviews.cus_home,name='cushome'),
    path('customer/bookcatagory',cviews.bookcatagory,name='bookcatagory'),
    path('add-to-cart/', cviews.add_to_cart, name='add_to_cart'),
    path("checkout/",cviews.checkout, name="checkout"),
    path("payment/", cviews.payment, name="payment"),
]