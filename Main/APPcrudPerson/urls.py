"""
URL configuration for APPCrud

"""
from django.contrib import admin
from django.urls import path

# Include the CRUD URLs from views.
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('create/', views.persona_create, name='persona_create'),
    path('list/', views.persona_list, name='persona_list'),
    path('update/<int:id>', views.persona_update, name='persona_update'),
    path('delete/<int:id>', views.persona_delete, name='persona_delete'),
]
