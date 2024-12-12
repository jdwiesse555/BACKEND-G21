from instancias import conexion
from sqlalchemy import Column,types, ForeignKey
from datetime import datetime


class Libro(conexion.Model):
    id = Column(type_=types.Integer,autoincrement=True,primary_key=True)
    titulo = Column(type_=types.Text ,nullable=False)
    descripcion  = Column(type_=types.Text)
    cantidad = Column(type_=types.Integer)
    disponible = Column(type_=types.Boolean)
    fechaCreacion = Column(type_=types.TIMESTAMP,default=datetime.now)
    categoriaId = Column(ForeignKey(column='categorias.id') ,
                          type_=types.Integer,nullable=True,name='categoria_id')

    __tablename__= 'libros'