from django.contrib import admin
from django.urls import path

def DesdeAppsPersona(self):
    print('============Desde la app personas============')

urlpatterns = [
    path('persona/',DesdeAppsPersona),
]