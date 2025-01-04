from django.shortcuts import render,redirect
from .models import Producto


# Create your views here.

def mostrarProductosPlantilla(request):
    # trae la data de base datos de table productos select * from productos
    Listaproductos = Producto.objects.all
    print(request)
    # aca hacemos una lista y las mostramos , solo se cambia Listaproducto por data
    data = [
        {
            'id':1,
            'nombre':'Lapiz Faber Castell',
            'descripcion':'Lapiz B2'

        },
        {
            'id':2,
            'nombre':'Resaltador color amarillo',
            'descripcion':None            
        }
    ]
    return render(request,'mostrar_productos.html',{'data':Listaproductos,'mensaje':'Bienvenido!'})

def crearProductosFormularios(request):
    if request.method == 'POST':
        #para recibir la info del formulario usamos request.POST.get con name
        print(request.POST)
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        print('quiere crear un producto')
        nuevoProducto = Producto(nombre=nombreProducto , descripcion=descripcionProducto)
        nuevoProducto.save()
        # como en teoria ya se creo el producto lo enviamos a ver los productos
        return redirect('mostrar_productos')
    

    elif request.method == 'GET':
        return render(request,'formulario_producto.html')
    
def editProductosFormularios(request,id=0):
    if request.method == 'POST':
        #para recibir la info del formulario usamos request.POST.get con name
        print(request.POST)
        idProducto = request.POST.get('idProducto')
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        print('quiere modificar un producto')
        nuevoProducto = Producto(id=idProducto, nombre=nombreProducto , descripcion=descripcionProducto)
        nuevoProducto.save()
        # como en teoria ya se creo el producto lo enviamos a ver los productos
        return redirect('mostrar_productos')
    

    elif request.method == 'GET':
        producto = Producto.objects.get(pk=id)
        return render(request,'modificar_producto.html',{'data':producto})

def delProductosFormularios(request,id=0):
    if request.method == 'POST':
        #para recibir la info del formulario usamos request.POST.get con name
        print(request.POST)
        
        producto = Producto.objects.get(pk=id)
        producto.delete()
        # como en teoria ya se creo el producto lo enviamos a ver los productos
        return redirect('mostrar_productos')
    

    elif request.method == 'GET':
        producto = Producto.objects.get(pk=id)
        return render(request,'borrar_producto.html',{'data':producto})
