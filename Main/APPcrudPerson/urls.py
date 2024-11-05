"""
URL configuration for APPCrud

"""
from django.contrib import admin
from django.urls import path

# Include the CRUD URLs from views.
from .views import ListaPersona, CreatePersonaView, PersonaUpdateView, index, IndexView, persona_create, persona_update

urlpatterns = [
    path('home/', IndexView.as_view(), name='index'),
    path('create/', CreatePersonaView.as_view(), name='create'),
    #path('create/', persona_create, name='create'),
    path('list/', ListaPersona.as_view(), name='list'),
    #path('update/<int:id>', persona_update, name='update'),
    path('update/<int:pk>', PersonaUpdateView.as_view(), name='update'),
    #path('delete/<int:id>', persona_delete, name='persona_delete'),
]
