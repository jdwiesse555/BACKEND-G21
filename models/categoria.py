from instancias import conexion
from sqlalchemy import Column, types
from sqlalchemy.orm import relationship


class Categoria(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False, unique=True)
    color = Column(type_=types.Text)
    #relationsship > sirve para poder ingresar a la relaciones que tiene la tabla en la bd sin la necesidad de hacer
    #una segunda consulta
    #el parametro backref nos crea un atributo en el otro modelo que estamos relacionando de manara virtual
    # es decir se creara ahora en la clase Libro un atributo con ese nombre para poder acceder
    libros = relationship('Libro',backref='categoria')

    __tablename__ = 'categorias'