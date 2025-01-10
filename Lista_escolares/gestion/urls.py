from django.urls import path
from .views import (mostrarProductosPlantilla,
                    crearProductosFormularios,
                    editProductosFormularios,
                    delProductosFormularios,
                    validarFuncionamiento,
                    ProductosControles,
                    ListarYCrearProductosControler,
                    DevolverActualizarEliminarProductoControler)

#para definr las rutas que van a comportarse en esta aplicacion usamos la variable urlpatterns
urlpatterns = [
    path('mostrar-productos',mostrarProductosPlantilla,name='mostrar_productos'),
    path('crear-producto',crearProductosFormularios,name='crear_producto'),
    path('edit-producto/<int:id>',editProductosFormularios,name='edit_producto'),
    path('borrar-producto/<int:id>',delProductosFormularios,name='borrar_producto'),
    # no se recomienda definie un name redicinamiento es diferente
    path('validar-funcionamiento',validarFuncionamiento),
    # al usar una clase tenemos que convertirna a una vista
    path('productos',ProductosControles.as_view()),
    path('productosv2',ListarYCrearProductosControler.as_view()),
    # solamente pk , si lo quiere cambiar en view lookup_fleld = 'id'
    path('producto/<id>',DevolverActualizarEliminarProductoControler.as_view()),
]