"""stageproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from . import views


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('yorumekle', views.review),
    path('register', views.register),
    path('urunekle', views.image_upload_view),
    path('login', views.Login),
    path('urunler/<slug:slug>', views.productpage, name='details'),
    path('urunler/', views.index),
    path('upload', views.image_upload_view),
    path('list', views.listview),
    path('ara', views.search),
    path('listtest', views.listtest),
    path('listpagination', views.listview_with_pagination),
    path("deneme",views.testing),
    path("ajaxlisting",views.ajaxlist,name="ajaxlist"),
    path("stack",views.stack)
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 