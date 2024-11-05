# Acá es dónde concetamos la capa de datos (los models)
# con las request y podemos enviar esa información
# a las vistas por medio de los protocolos http.
# GET-POST-PUT-PATCH-DELETE.

""" --- LA RUTA QUE SIGUE DJANGO CON Las VISTAS BASADAS EN CLASES.---
        1.- dispatch(): se encarga de recibir la peticion y elegirla.
        2.- http_method_not_allowed(): retorna u error cuando se utilizada uin metodo http nop soportado.
        3.- options():
"""

from typing import Any
from urllib import request
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from .models import Persona # Importamos el modelo persona para poder trabajar con los metodos HTTP.
from django.views.decorators.csrf import csrf_exempt #Agregamos esta línea para decirle que no necesitamos el token de seguridad ya que es local.
from django.views.generic import View, ListView, TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .forms import PersonaForm

#Index
def index(request):
    print("Loading index")
    if request.method == 'GET':
        HttpResponse(status=200, content="Index cargado exitosamente.")
        return render(request, 'APPcrudPerson/index.html')
    else:
        return HttpResponseNotFound(status=405 , content="Método no permitido.")

#Index basado en clases.
class IndexView(TemplateView):
    print("Loading index")
    template_name = 'APPcrudPerson/index.html'
    
#Lista por medio de un método.
def persona_list(request):
    print("Loading persona list")
    personas = Persona.objects.all()
    try:
        data = {
        'personas' : personas,
        }
        return render(request, 'APPcrudPerson/list.html', data)
    except Persona.DoesNotExist:
        raise Http404("En personas, no hay nada.-")
    
#Lista basada en clases.
class ListaPersona(ListView):
    model = Persona
    template_name = 'APPcrudPerson/list.html'

    
    def get_queryset(self):
        return Persona.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['personas'] = Persona.objects.all()
        return context

############################################################################################################
#Create persona basado en clases.
class CreatePersonaView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'APPcrudPerson/create.html'
    #Retornamos un mensaje cuando se crea una persona.
    print("Persona creada exitosamente...")
    success_url = reverse_lazy('list')

    # #Validamos el formulario
    # def form_valid(self, form):
    #     print("Validando formulario...")
    #     form.instance.save()
    #     print("Persona creada -->:", form.instance)
    #     return super().form_valid(form)



############################################################################################################
@csrf_exempt
def persona_create(request):
    print("Loading method persona create")
    try:
        id=11
        nombre = "Marcelo"
        apellido = "Delgado"
        edad = 51
        hobbie = "Futbolista"
        tipo_documento = "DNI"
        numero_documento = 23566610
        persona = Persona.objects.create(id=id, nombre=nombre, apellido=apellido, edad=edad, hobbie=hobbie, tipo_documento=tipo_documento, numero_documento=numero_documento)
        return HttpResponse(status=201, content="Persona creada exitosamente.")
    except Exception as e:
        print("Error al crear la persona: ", str(e))
        return HttpResponse(status=400, content="Error al crear la persona.")
    
################################################################################################################    
@csrf_exempt
def persona_update(request, id):
    print("Buscando a persona con el id: " + str(id))
    try:
        persona = get_object_or_404(Persona, numero_documento=id)
        print("La encontré. Toma los detalles: ", persona)
        nombre = "Marcelo Daniel"
        persona = Persona.objects.update_or_create()
        print("Persona modificada -->:", persona)
        return HttpResponse(status=200, content="Persona modificada exitosamente.")
        #return render(request, 'APPcrudPerson/list.html', {'persona': persona})
    except Persona.DoesNotExist:
        raise Http404("La persona con el id no existe.-")
    
class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = "APPcrudPerson/create.html"
    form_class = PersonaForm
    success_url = reverse_lazy('APPcrudPerson: list')

@csrf_exempt
def persona_delete(request, id):
    print("Buscando a persona con el id: " + str(id))
    try: 
        if request.method == 'DELETE':
            persona = Persona.objects.get(numero_documento=id)
            print("La encontré. Toma los detalles: ", persona)
            persona.delete()
            print("Persona eliminada.")
            return HttpResponse(status=200, content="Persona eliminada exitosamente.")
    except:
        return HttpResponse(status=404, content="La persona con el id no existe.-")


class PersonaDeleteView(DeleteView):
    model = Persona
    #template_name = "APPcrudPerson/delete.html"
    success_url = reverse_lazy('APPcrudPerson:list')
    
    def post(self, request, pk, *args, **kwargs):
        object = Persona.objects.get(id=pk)
        object.delete()
        object.save()
        return HttpResponse(status=200, content="Persona eliminada exitosamente.")
    

