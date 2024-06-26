"""
URL configuration for A3Django project.

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

import app.views

urlpatterns = [
    path('user/getUserInfo/', app.views.get_user_info),
    path('user/login/', app.views.login),
    path('user/register/', app.views.register),
    path('user/updateUserInfo/', app.views.update_user_info),
    path('user/updateUserPassword/', app.views.update_user_password),
    path('flights/getFlightsPage/', app.views.get_flights_page),
    path('admin/', admin.site.urls),

]
