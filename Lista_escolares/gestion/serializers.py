from rest_framework.serializers import ModelSerializer
from .models import Producto
# hay dos formas : con modelo o sin modelo

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto


        fields = '__all__'
        # otra forma de definir los atributos 
        #exclude = ['id','descripcion']

