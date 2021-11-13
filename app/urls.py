from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'clinics', views.ClinicViewSet)
router.register(r'applications', views.ApplicationViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]