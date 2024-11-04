# Acá es dónde concetamos la capa de datos (los models)
# con las request y podemos enviar esa información
# a las vistas por medio de los protocolos http.
# GET-POST-PUT-PATCH-DELETE.

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from .models import Persona # Importamos el modelo persona para poder trabajar con los metodos HTTP.
from django.views.decorators.csrf import csrf_exempt #Agregamos esta línea para decirle que no necesitamos el token de seguridad ya que es local.

def index(request):
    print("Loading index")
    if request.method == 'GET':
        HttpResponse(status=200, content="Index cargado exitosamente.")
        return render(request, 'APPcrudPerson/index.html')
    else:
        return HttpResponseNotFound(status=405 , content="Método no permitido.")

def persona_list(request):
    print("Loading persona list")
    try:
        personas = Persona.objects.all()
        return render(request, 'APPcrudPerson/list.html', {'personas': personas})
    except Persona.DoesNotExist:
        raise Http404("En personas, no hay nada.-")
        
@csrf_exempt
def persona_create(request):
    print("Loading method persona create")
    try:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        hobbie = request.POST['hobbie']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        persona = Persona.objects.create(nombre=nombre, apellido=apellido, edad=edad, hobbie=hobbie, tipo_documento=tipo_documento, numero_documento=numero_documento)
        return HttpResponse(status=201, content="Persona creada exitosamente.")
    except:
        return HttpResponse(status=400, content="Error al crear la persona.")
@csrf_exempt
def persona_update(request, id):
    print("Buscando a persona con el id: " + str(id))
    try:
        persona = Persona.objects.get(numero_documento=id)
        print("La encontré. Toma los detalles: ", persona)
        if request.method == 'POST':
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            edad = request.POST['edad']
            hobbie = request.POST['hobbie']
            persona.save()
            print("Persona modificada -->:", persona)
            return HttpResponse(status=200, content="Persona modificada exitosamente.")
        return render(request, 'APPcrudPerson/list.html', {'persona': persona})
    except Persona.DoesNotExist:
        raise Http404("La persona con el id no existe.-")

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

