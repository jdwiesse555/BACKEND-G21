from instancias import conexion
from sqlalchemy import Column,types
from enum import Enum

class tipousuario(Enum) :
    ADMIN='ADMIN'
    CLIENTE='CLIENTE'
    EMPLEADO ='EMPLEADO' 

class Usuario(conexion.Model):
    id = Column(type_=types.Integer,autoincrement=True,primary_key=True)
    nombre = Column(type_=types.Text)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text,unique=True)
    password = Column(type_=types.Text,nullable=False)
    tipo_usuario = Column(type_=types.Enum(tipousuario),
                          default=tipousuario.CLIENTE)


    __tablename__= 'usuarios'
    __bind_key__='mysql'
