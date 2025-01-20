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
    path('add_book/',pubviews.add_book,name='add_book'),
    # path('customer/',include('customer.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
