from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    # loa campos que voy a mostrar de mi table producto
    list_display = ['nombre']
    # los campos que voy a trabajar
    fields = ['nombre','descripcion']
# Register your models here.
#aca indico que modelo de esta aplicacopn puedo gestionar en el panel adminstrativo
admin.site.register(Producto,ProductoAdmin)