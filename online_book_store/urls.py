"""
URL configuration for online_book_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home import views as hviews
from publisher import views as pubviews
from django.conf.urls.static import static
from django.conf import settings
from customer import views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('',hviews.home,name='home'),
    path('about/',hviews.about,name='about'),
    path('contact/',hviews.contact,name='contact'),
    path('gallery/',hviews.gallery,name='gallery'),
    path('faq/',hviews.faq,name='faq'),
    path('login/',include('login.urls')),
    #publisher
    path('pub_home/',include('publisher.urls')),
    path('addbook/',pubviews.addbook,name='addbook'),
    path('customer/',include('customer.urls')),
    path("add_to_cart/", cviews.add_to_cart, name="add_to_cart"),
    path("cart/",cviews.view_cart, name="cart"),
    path("remove_from_cart/", cviews.remove_from_cart, name="remove_from_cart"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
