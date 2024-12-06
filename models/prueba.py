from instancias import conexion
from sqlalchemy import Column,types



class PruebaModel(conexion.Model):
    id =  Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text, nullable=True)
    precio = Column(type_=types.Float,nullable=False)
    disponibilidad = Column(type_=types.Boolean,  default=True)
    
    __tablename__ = 'prueba'
    __bind_key__='postgres2'