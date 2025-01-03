"""
URL configuration for know_about_iran project.

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
from home_page import urls as home_page_u
from main_page import urls as main_page_u
urlpatterns = [
    path('main',include(home_page_u)),
    path('admin/', admin.site.urls),
    path('home/',include(main_page_u)),
    path("",include(main_page_u))
    
]
#