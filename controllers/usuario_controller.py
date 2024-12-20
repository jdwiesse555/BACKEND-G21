from flask_restful import Resource,request
from models import Usuario
from instancias import conexion
from .serializers import (RegistroSerializer,LoginSerialize,
                          UpdateSerialize,OlvidePasswordSerialize)
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt,hashpw,checkpw
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity





class RegistroController(Resource):

    serializador = RegistroSerializer()
    def post(self):
        data = request.get_json()
        
        try:
          
            data_serializada = self.serializador.load(data)
            # Generar el hash de la password para guardarla en la bd
            salt = gensalt()
            
            password_hashed = hashpw(
                bytes(data_serializada.get('password'),'utf-8'),salt).decode('utf-8')
             # ahora reemplazamos el valor de la password con el hasheo de la password
            data_serializada['password']= password_hashed
            nueva_usuario = Usuario(**data_serializada)
            conexion.session.add(nueva_usuario)
            conexion.session.commit()

            resultado = self.serializador.dump(nueva_usuario)

            return {
                'message':'Ususario creada exitosamente',
                'content': resultado
            }

        except ValidationError as error:
            return {
                'mensage':'Error al crear la Usuario',
                'content': error.args
            }
    

    def get(self):
        # select * from usuarios
        usuarios = conexion.session.query(Usuario).all()
        
        return {
            'content' :  self.serializador.dump(usuarios, many=True)
        }       
    
class LoginController(Resource):
    def post(self):
        data = request.get_json()
        serializador = LoginSerialize()
        try:
            data_serializada = serializador.load(data)
            # Buscamos si el usuario existe en la bd
            usuario_encontrado = conexion.session.query(Usuario).filter(
                Usuario.correo== data_serializada.get('correo')
            ).first()
            if usuario_encontrado is None:
                return {
                    'message':'El usuario no existe'
                }
            password_en_bytes = bytes(data_serializada.get('password'),'utf-8')
            password_db_en_bytes =  bytes(usuario_encontrado.password, 'utf-8')
             # el checkpw contrastara la password guardada en la bd con la password enviada en el login y si es, retornara True, caso contrario, False
            resultado = checkpw(password_en_bytes,password_db_en_bytes)
            if resultado == True:
                #identity > es el identificador para reconoser a que usaurio le pertenece esa token
                #el identity siemplre debe ser un spring
                token=create_access_token(identity=str(usuario_encontrado.id))
                return {
                    'message':'Bienvenido',
                    'token':token
                }
            else:
                return {
                    'message':'Cresdenciales incorrectas'
                }
        except ValidationError as error:
            return {
                'message':'Error al hacer login',
                'content': error.args
            }    

class UsuarioController(Resource):
    #este metodo geT es una ruta protegida, necesita un token para ingresar
    @jwt_required()
    def get(self):
        identificador = get_jwt_identity()
        
        usuario_encontrado = conexion.session.query(Usuario).filter(Usuario.id==identificador).first()
        if usuario_encontrado is None:
            return {
                'message':'El usuario no existe'
            }
        serializador = RegistroSerializer()
        resultado = serializador.dump(usuario_encontrado)
        
        return {
            'content': resultado  #retornar el usuario 
        }
    
    @jwt_required()
    def put(self):
        #actualizar el usuario
        identificador = get_jwt_identity()
        
        usuario_encontrado = conexion.session.query(Usuario).filter(Usuario.id==identificador).first()
        if usuario_encontrado is None:
            return {
                'message':'El usuario no existe'
            }
        data = request.get_json()
        serializador = UpdateSerialize()
        try: 
            data_validada = serializador.load(data)
            usuario_encontrado.nombre = data_validada.get(
                'nombre') if data_validada.get('nombre') else usuario_encontrado.nombre 
            usuario_encontrado.apellido = data_validada.get(
                'apellido') if data_validada.get('apellido') else usuario_encontrado.apellido 

            if data_validada.get('password'):
                salt = gensalt()
                password_en_bytes = bytes(
                    data_validada.get('password'),'utf-8'
                )
                password_hasheada = hashpw(
                    password_en_bytes,salt
                ).decode('utf-8')
                usuario_encontrado.password = password_hasheada
            resultado = serializador.dump(usuario_encontrado)
            conexion.session.commit()
            return {
                'message': 'Usuario actualizada exitosamente',
                'content': resultado
            }
        except ValidationError as error:
            return {
                'message': 'Error al actualizar la Usuario',
                'content': error.args
            }    

        #modificar el nombre y password mas no el correo
        #crear un seriealizado Manual en el cual vamos a indicar que recibimos el nomnre de password ambos e caracter opcional
        # en la base  a la verificacion del serializacion vamos a hacer la actualizacion de nuestro usaurio
       
class OlvidePasswordComtroller(Resource):
    def post(self):
        serializador = OlvidePasswordSerialize()
        try:
            data_serializada = serializador.load(request.get_json())
            usuario_encontrado = conexion.session.query(Usuario).filter(
                Usuario.correo == data_serializada.get('correo')).with_entities(Usuario.id).first()
            if usuario_encontrado is None:
                return{
                    'message':'Usuario no se encuentra en la BD' 
                }

            return {
                'message':'Correo enviado con las indicaciones'
            }
        except ValidationError as error:
            return {
                'message':'Usuario al ejecutar el olvido de password',
                'content':error.args
            }

        return {
            'message': 'Correo enviado con las indicaciones'
        }


    