from django.urls import path
from  customer  import views as cviews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
     path('cus_home',cviews.cus_home,name='cushome'),
    path('bookcatagory',cviews.bookcatagory,name='bookcatagory'),
    path("add_to_cart/", cviews.add_to_cart, name="add_to_cart"),
    path("cart/",cviews.view_cart, name="cart"),
    path("remove_from_cart/", cviews.remove_from_cart, name="remove_from_cart"),
    path("checkout/",cviews.checkout, name="checkout"),
    path("payment/", cviews.payment, name="payment"),
    path("payment-options/", cviews.payment_options, name="payment_options"),
    path("process-payment/", cviews.process_payment, name="process_payment"),
    path("credit-card-payment/",cviews.credit_card_payment, name="credit_card_payment"),
    path("paypal-payment/", cviews.paypal_payment, name="paypal_payment"),
    path("cod-success/",cviews.cod_success, name="cod_success"),
    path("order_success/",cviews.order_success, name="order_success"),
]