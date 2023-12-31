"""
URL configuration for restaurantproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.contrib import admin
from restaurantapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from restaurantapp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('menu/',views.menu,name='menu'),
    path('join/',views.join,name='join'),
    path('adduser',views.adduser,name='adduser'),
    path('biryani/',views.biryani,name='biryani'),
    path('test',views.test,name='test'),
    path('addData',views.addData,name='addData'),
    path('login',views.login,name='login'),
     path('useraccess',views.useraccess,name='useraccess')
    

    
    

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)