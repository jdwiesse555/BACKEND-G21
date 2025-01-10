from django.shortcuts import render,redirect
from .models import Producto
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ProductoSerializer



# Create your views here.

    


def mostrarProductosPlantilla(request):    
   
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('')

    # trae la data de base datos de table productos select * from productos
    Listaproductos = Producto.objects.all
    
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
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('')
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
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('')
    if request.method == 'POST':
        #para recibir la info del formulario usamos request.POST.get con name
        print(request.POST)
        idProducto = request.POST.get('idProducto')
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        print('quiere modificar un producto')
        producto = Producto.objects.get(pk=id)
        if producto :
            producto.nombre=nombreProducto
            producto.descripcion=descripcionProducto
            producto.save()
        # como en teoria ya se creo el producto lo enviamos a ver los productos
        return redirect('mostrar_productos')
    

    elif request.method == 'GET':
        producto = Producto.objects.get(pk=id)
        return render(request,'modificar_producto.html',{'data':producto})

def delProductosFormularios(request,id=0):
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('')
    if request.method == 'POST':
        #para recibir la info del formulario usamos request.POST.get con name
        print(request.POST)
        
        producto = Producto.objects.get(pk=id)
        if producto :
            producto.delete()
        # como en teoria ya se creo el producto lo enviamos a ver los productos
        return redirect('mostrar_productos')
    

    elif request.method == 'GET':
        producto = Producto.objects.get(pk=id)
        return render(request,'borrar_producto.html',{'data':producto})

@api_view(http_method_names=['GET','POST'])
def validarFuncionamiento(request):
    # este request que nos llega usando rest_frameword es un request diferencte a la de as plantillas,porque usa la libreria
    #https://www.django-rest-framework.org/api-guide/requests/
    if request.method == 'GET':

        return Response(data={
            'message': 'El servidor funcion exitosamente'
        })
    elif request.method == 'POST':
        print(request.data)
        return Response(data={
            'message':'Informacion aceptada correctamente'
        })
# al usar generic apiview ws similar a lo que hacianos flask Resouce
class ProductosControles(GenericAPIView):
    def get(seft,request):
        productos=Producto.objects.all()
        serializador = ProductoSerializer(productos, many=True)
        serializador.data
        
        return Response(data={
            'message':'Los priduc)tos son',
            'content':serializador.data
        })
    def post(self, request):
        # la data provien del request
        data = request.data
        serializador = ProductoSerializer(data=data)
        # ahora queremos validar si la informacion es valida is_valid()
        if serializador.is_valid():
            #usando model serializar en mu fasil
            serializador.save()
            return Response(data={
                'message':'Producto creado exitosamente'
            })

        else:
            #si no es valida
            # si envia error
            return Response(data={
                'message':'Error al crear el producto',
                'content': serializador.errors
            })
        
class ListarYCrearProductosControler(ListCreateAPIView) :
    #Para utilizar una vista generica se tiene que definir los siguientes atributos
    #como obtendra la informacion y la devolvera
    queryset = Producto.objects
    #Para indicar como tiene que validar y devolver la informacion proviniente de bd
    serializer_class = ProductoSerializer

class DevolverActualizarEliminarProductoControler(RetrieveUpdateDestroyAPIView) :
    #Para utilizar una vista generica se tiene que definir los siguientes atributos
    #como obtendra la informacion y la devolvera
    queryset = Producto.objects
    #Para indicar como tiene que validar y devolver la informacion proviniente de bd
    serializer_class = ProductoSerializer
    lookup_field = 'id'

 