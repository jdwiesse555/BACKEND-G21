from flask_restful import Resource,request
from models import ProductoModel
from instancias import conexion
from .serializers import ProductoSerializer}}
from marshmallow.exceptions import ValidationError

class ProductoController(Resource):
    def get(self):
        #select * from categorias
        data = conexion.session.query(ProductoModel).all()
        # convertir la informacion de instancia a un diccionario para devlver usando marshmallow
        serializador = ProductoSerializer()
        resultado = serializador.dump(data, many=True)
        return {
            'message':'los Productos son',
            'result':resultado
        }
    def post(self):
        #obtenemos la inf de body previamente del request
        data = request.get_json()
        serializador = ProductoSerializer()
        try:
            #carga la informacion y la validad
            data_serializada= serializador.load(data)
            # quiero pasar un dic parametros de una funcion
            nueva_producto=ProductoModel(**data_serializada)

            #agregar en la dase datos
            conexion.session.add(nueva_producto)
            conexion.session.commit()

            resultado = serializador.dump(nueva_producto)
            return {
                'message': 'Producto creada exitosamente',
                'content': resultado
            }

        except ValidationError as error:
            return {
                'message':'Error al crear la Producto',
                'content': error.args
            }  
