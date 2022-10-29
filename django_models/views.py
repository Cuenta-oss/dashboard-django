from django.http import Http404
from django.shortcuts import redirect, render
from .forms import contactForm, productoForm
from .models import infoProducto
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

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
    if request.method == 'GET':
        form = productoForm
        template_name = 'infoProducto.html'
        data = {
            'form': form
        }
        return render(request, template_name, data)
    else:
        try:
            formulario = productoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.add_message(request, messages.SUCCESS, "Nuevo producto añadido")
                return redirect('list_productos')
        except:
            data = {
                'form' : form,
                'error' : 'Error al guardar el producto'
            }
        return render(request, template_name, data)


def listProduct(request):
    template_name = 'registrosProd.html'
    data = infoProducto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(data, 5)
        data = paginator.page(page)
    except:
        return Http404
    context = {
        'entity' : data,
        'paginator':paginator
    }
    return render(request, template_name, context)

def editProduct(request, id):
    template_name = 'editProduct.html'
    if request.method == 'GET':
        producto = infoProducto.objects.get(id=id)
        formulario = productoForm(instance=producto)
        data = {
            'form' : formulario
        }
        return render(request, template_name, data )
    else:
        try:
            producto = infoProducto.objects.get(id=id)
            formulario = productoForm(request.POST, instance=producto)
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Producto modificado')
            return redirect('list_productos')
        except ValueError:
            data = {
                'producto' : producto,
                'form' : formulario,
                'error' : 'No se pudo actualizar'
            }
            return render(request, template_name, data )
        
def del_product(request, id):
    
    producto = infoProducto.objects.get(id=id)
    producto.delete()
    messages.add_message(request, messages.SUCCESS, "Eliminado correctamente")
    return redirect('list_productos')
    """ if request.method == 'GET':
        producto = infoProducto.objects.get(id=id)
        data = {
            'producto' : producto
        }
        return redirect('list_productos')
    else:
        try:
            producto = infoProducto.objects.get(id=id)
            producto.delete()
            return redirect('list_productos')
        except:
            data = {
                'producto' : producto,
                'error' : 'Ocurrio un error'
            }
            return redirect('list_productos') """
    