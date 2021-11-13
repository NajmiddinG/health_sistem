from django.contrib import admin
from .models import Clinic, Department, Doctor, Client, Application

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'tell']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'clinic', 'name']

@admin.register(Doctor)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'first_name', 'last_name', 'password', 'tell']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'password', 'tell']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'doctor', 'message', 'time', 'order', 'status']
