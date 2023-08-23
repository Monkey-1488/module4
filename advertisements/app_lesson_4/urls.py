from django.urls import path
from .views import func_dz

urlpatterns = [
    path('', func_dz)
]