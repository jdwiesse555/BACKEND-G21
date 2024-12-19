from flask_restful import Resource,request
from models import Usuario
from instancias import conexion
from .serializers import RegistroSerializer,LoginSerialize
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt,hashpw,checkpw



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
                return {
                    'message':'Bienvenido'
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

