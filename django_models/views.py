from urllib import request
from django.shortcuts import render
from .forms import contactForm, productoForm
from .models import infoProducto


def about(request):
    template_name = 'about.html'
    return render(request, template_name)


def contact(request):
    form = contactForm()
    data = {
        'form': form,
    }
    if request.method == 'POST':
        formulario = contactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contact save"
        else:
            data["mensaje"] = "ERROR! ocurred"
    template_name = 'contact.html'
    return render(request, template_name, data)


def addProduct(request):
    form = productoForm
    template_name = 'infoProducto.html'
    data = {
        'form': form
    }
    if request.method == 'POST':
        formulario = productoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Producto guardado'
        else:
            data['mensaje'] = "Error al guardar el producto"
    return render(request, template_name, data)


def listProduct(request):
    template_name = 'registrosProd.html'
    data = infoProducto.objects.all()
    context = {
        'data' : data
    }
    return render(request, template_name, context)
