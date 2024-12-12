from flask_restful import Resource,request
from models import CategoriaModel
from instancias import conexion
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError

class CategoriaControlles(Resource):
    def get(self):
        #select * from categorias
        data = conexion.session.query(CategoriaModel).all()
        # convertir la informacion de instancia a un diccionario para devlver usando marshmallow
        serializador = CategoriaSerializer()
        resultado = serializador.dump(data, many=True)
        return {
            'message':'las Categorias son',
            'result':resultado
        }
    def post(self):
        #obtenemos la inf de body previamente del request
        data = request.get_json()
        serializador = CategoriaSerializer()
        try:
            #carga la informacion y la validad
            data_serializada= serializador.load(data)
            # quiero pasar un dic parametros de una funcion
            nueva_categoria=CategoriaModel(**data_serializada)

            #agregar en la dase datos
            conexion.session.add(nueva_categoria)
            conexion.session.commit()

            resultado = serializador.dump(nueva_categoria)
            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }

        except ValidationError as error:
            return {
                'message':'Error al crear la Categoria',
                'content': error.args
            }    
        
class ManejoCategoriaController(Resource):
    def validarCategoria(self,id):
        categoria_encontrada = conexion.session.query(CategoriaModel).filter(
            CategoriaModel.id==int(id)).first()  

        
        return {'message':'categoria no existe'} if categoria_encontrada is None else categoria_encontrada
        
 
    def get(self,id):
       categoria_encontrada=self.validarCategoria(id)

       if type(categoria_encontrada)== dict:
           return categoria_encontrada
       
       serializador = CategoriaSerializer()
       resultado = serializador.dump(categoria_encontrada)
       
       return {
           'content':resultado
       }
    
    def put(self,id):
       
       categoria_encontrada=self.validarCategoria(id)
       if type(categoria_encontrada)== dict:
           return categoria_encontrada
       data = request.get_json()
       serializador = CategoriaSerializer()
       try:
            #carga la informacion y la validad
            data_validada= serializador.load(data)
            # quiero pasar un dic parametros de una funcion
            categoria_encontrada.nombre = data_validada.get('nombre')
            categoria_encontrada.disponibilidad = data_validada.get('disponibilidad') if data_validada.get(
                'disponibilidad') is not None else categoria_encontrada.disponibilidad

            #agregar en la dase datos
            
            conexion.session.commit()

            resultado = serializador.dump(categoria_encontrada)
            return {
                'message': 'Categoria modificaada exitosamente',
                'content': resultado
            }

       except ValidationError as error:
            return {
                'message':'Error al actualizar la Categoria',
                'content': error.args
            }    
        
 
    def delete(self,id):
       
       categoria_encontrada=self.validarCategoria(id)
       if type(categoria_encontrada)== dict:
           return categoria_encontrada
       data = request.get_json()
       serializador = CategoriaSerializer()
       try:


            #agregar en la dase datos
            conexion.session.delete(categoria_encontrada)
            conexion.session.commit()

            resultado = serializador.dump(categoria_encontrada)
            return {
                'message': 'Categoria borrada exitosamente',
                'content': resultado
            }

       except ValidationError as error:
            return {
                'message':'Error al actualizar la Categoria',
                'content': error.args
            }    
        
 
