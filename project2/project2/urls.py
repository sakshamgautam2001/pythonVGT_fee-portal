"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome),
    path('student_reg/',student_reg),
    path('show_data/',show_data),
    path('edit_data/',edit_data),
    path('login/',login),
    path('admin_home/',admin_home),
    path('student_home/',student_home),
    path('auth_error/',auth_error),
    path('logout/',logout),
    path('admin_reg/',admin_reg),
    path('edit_data1/',edit_data1),
    path('upload_photo/',upload_photo),
    path('change_password/',change_password),
    path('employee_reg/',employee_reg),
    path('employee_home/',employee_home),
    path('search_student/',search_student),
    path('change_photo/',change_photo),
    path('edit_request/',edit_request),
    path('show_request/',show_request),
    path('fees_deposit/',fees_deposit),
    path('rest_fees/',rest_fees),
    path('due_fees/',due_fees),
    path('delete_data/',delete_data),
    path('delete_photo/',delete_photo),
    path('go_home/',go_home),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



