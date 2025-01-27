from django.urls import path
from apps.diagnostico_gms.views import index

urlpatterns = [
    path('', index),
]