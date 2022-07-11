from django.shortcuts import render, get_object_or_404  # importocion de librerias
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from MoniApp.models import Pedido_prestamo
from MoniApp.forms import FormPedido_prestamo
from MoniApp.models import Imagenes
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests, json

# Create your views here.


def home(request):

    # Todos los objetos  de la class Imagenes y lo guardamos dentro de la variable.
    imagenes = Imagenes.objects.all()

    # Crea el html con los datos que estan en la variable servicios.
    return render(request, "moniApp/home.html", {"imagenes": imagenes})


def crearForm(request):

    if request.method == "POST":
        form = FormPedido_prestamo(request.POST)
        if form.is_valid():
            try:
                nombre = form.cleaned_data['nombre']
                apellido = form.cleaned_data['apellido']
                dni = form.cleaned_data['dni']
                genero = form.cleaned_data['genero']
                email = form.cleaned_data['email']
                monto = form.cleaned_data['monto']

                Pedido_prestamo(nombre=nombre, apellido=apellido, dni=dni,
                                genero=genero, email=email, monto=monto).save()

                messages.success(request, 'La solicitud fue enviada con exito!!')

                """url= 'https://api.moni.com.ar/api/v4/scoring/pre-score/'
                payload = {'dni':dni}
                headers = {'credential':'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}

                response = requests.post(url, data=json.dumps(payload),headers=headers)

                if response.status_code == 200:
                    messages.success(request, response.content)"""

            except:
                messages.error(request, 'Se produjo un error al guardar')

            return HttpResponseRedirect("/crearForm/")

    elif request.method == "GET":
        form = FormPedido_prestamo()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    return render(request, 'moniApp/crearForm.html', {'form': form})

@login_required
def listado(request):

    prestamos = Pedido_prestamo.objects.all()

    return render(request, 'moniApp/listado.html', {"prestamos": prestamos})


def actualizar(request, identificador):
    prestamoId = Pedido_prestamo.objects.get(id=identificador)

    if request.method == "POST":
        form = FormPedido_prestamo(request.POST)
        if form.is_valid():
            try:
                prestamoId.nombre = form.cleaned_data['nombre']
                prestamoId.apellido = form.cleaned_data['apellido']
                prestamoId.dni = form.cleaned_data['dni']
                prestamoId.genero = form.cleaned_data['genero']
                prestamoId.email = form.cleaned_data['email']
                prestamoId.monto = form.cleaned_data['monto']
                prestamoId.save()

                messages.success(request, 'La actualización se ha realizado con éxito!')
            except (RuntimeError):
                messages.error(request, "Hubo un error al guardar")
            # return render(request, 'actualizarDatosPersona.html', context_instance=RequestContext(request))
            return HttpResponseRedirect(reverse("listado"))
    elif request.method == "GET":
        form = FormPedido_prestamo(initial={'nombre': prestamoId.nombre, 'apellido': prestamoId.apellido,
                'dni': prestamoId.dni, 'genero': prestamoId.genero, 'email': prestamoId.email, 'monto': prestamoId.monto})
        if form.is_valid():
            contexto = {'form': form}
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request " + request.method)

    return render(request, 'moniApp/actualizar.html', {'form': form})



def borrar(request, identificador):

    if request.method == "GET":
        prestamo = Pedido_prestamo.objects.filter(id=int(identificador)).first()
        if prestamo:
            prestamo.delete()
        messages.success(request, 'El borrado se realizo con éxito')
        return HttpResponseRedirect(reverse("listado"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")






"""    if request.method == "GET":
            prestamo = get_object_or_404(Pedido_prestamo, pk=int(identificador))
            initial={'nombre': prestamo.nombre, 'apellido': prestamo.apellido,
                'dni': prestamo.dni, 'genero': prestamo.genero, 'email': prestamo.email, 'monto': prestamo.monto}

            form_actualizar = ActualizarFormPedido_prestamo(initial=initial)
            return render(request, 'moniApp/actualizar.html', {'form': form_actualizar, 'actualizar': True})

    elif request.method == "POST":
        form_actualizar = ActualizarFormPedido_prestamo(request.POST)
        if form_actualizar.is_valid():

            prestamo = get_object_or_404(Pedido_prestamo, pk=form_actualizar.cleaned_data['id'])
            prestamo.nombre = form_actualizar.cleaned_data['nombre']
            prestamo.apellido = form_actualizar.cleaned_data['apellido']
            prestamo.dni = form_actualizar.cleaned_data['dni']
            prestamo.genero = form_actualizar.cleaned_data['genero']
            prestamo.email = form_actualizar.cleaned_data['email']
            prestamo.monto = form_actualizar.cleaned_data['monto']

            prestamo.save()

            return HttpResponseRedirect(reverse("listado"))"""

