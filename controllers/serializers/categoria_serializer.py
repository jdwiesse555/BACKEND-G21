from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import CategoriaModel

class CategoriaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        # Pasale metadatos a la clase de la cual estamos heredando
        model = CategoriaModel
