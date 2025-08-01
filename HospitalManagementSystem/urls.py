"""HospitalManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from hospitals.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name="about"),
    path('',Index,name='index'),
    path('contact', contact, name='contact'),
    path('login', adminlogin, name='login'),
    path('admin_home', admin_home, name='admin_home'),
    path('logout', Logout, name='logout'),
    path('add_doctor', add_doctor, name='add_doctor'),
    path('view_doctor/', view_doctor, name='view_doctor'),
    path('delete_doctor/<int:id>', delete_doctor, name='delete_doctor'),
    path('add_patient', add_patient, name='add_patient'),
    path('view_patient', view_patient, name='view_patient'),
    path('delete_patient/<int:pid>', delete_patient, name='delete_patient'),
    path('add_appointment', add_appointment, name='add_appointment'),
    path('view_appointment', view_appointment, name='view_appointment'),
    path('delete_appointment/<int:pid>', Delete_Appointment, name='delete_appointment'),
    path('edit_doctor/<int:pid>',edit_doctor,name='edit_doctor'),
    path('edit_patient/<int:pid>',edit_patient,name='edit_patient'),
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_query/<int:contact_id>/', view_query, name='view_query'),  # ✅ correct

    path('bed_details/', bed_details, name='bed_details'),
    path('add_payment/', add_payment, name='add_payment'),
    path('view_payments/', view_payments, name='view_payments'),
    path('edit_payment/<int:id>/', edit_payment, name='edit_payment'),
    path('delete_payment/<int:id>/', delete_payment, name='delete_payment'),
    path('download_receipt/<int:id>/', download_receipt, name='download_receipt'),

]