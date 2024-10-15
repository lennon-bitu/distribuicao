# distribution/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.transfer_form, name='transfer_form'),
    path('label/<int:pk>/', views.label_print, name='label_print'),
]
