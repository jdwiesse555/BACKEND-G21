from django.urls import path
from .views import (mostrarProductosPlantilla,crearProductosFormularios,editProductosFormularios,delProductosFormularios)

#para definr las rutas que van a comportarse en esta aplicacion usamos la variable urlpatterns
urlpatterns = [
    path('mostrar-productos',mostrarProductosPlantilla,name='mostrar_productos'),
    path('crear-producto',crearProductosFormularios,name='crear_producto'),
    path('edit-producto/<int:id>',editProductosFormularios,name='edit_producto'),
    path('borrar-producto/<int:id>',delProductosFormularios,name='borrar_producto')
]