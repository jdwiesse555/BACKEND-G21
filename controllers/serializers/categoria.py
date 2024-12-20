from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Categoria
from marshmallow import fields
from .libro_serialiers import LibroSerializer

class CategoriaSerializer(SQLAlchemyAutoSchema):
    # si utilizamos un atribuye que no esta debidamente identificado en el modelo,
    # entonce temos que utulizar l paramenteo attibute
    #libros = fields.Nested(LibroSerializer, many=True)
    librosDeLaCategoria = fields.Nested(LibroSerializer, many=True,attribute='libros')
    class Meta:
        model = Categoria
        # si queremos que este serializador incluya las relaciones
        #include_relationships = True
        # si utilizamos attibute  ya no se include_ralationships