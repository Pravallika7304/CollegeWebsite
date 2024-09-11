"""
URL configuration for miniproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app1.views import index,about,contactus,register,doregister,login,logincheck,docontact,adminhome,userhome,viewusers,modify,placements,more
admin.site.site_header="GIST Admin"
admin.site.site_title = "GIST Admin Portal"
admin.site.index_title = "Welcome to GIST"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path("register/",register),
    path("doregister/",doregister),
    path("about/",about),
    path("placements/",placements),
    path("contactus/",contactus),
    path("docontact/",docontact),
    path("login/",login),
    path("logincheck/",logincheck),
    path("adminhome/",adminhome),
    path("userhome/",userhome),
    path("viewusers/",viewusers),
    path("modify/",modify),
    path("more/",more),

]