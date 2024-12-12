from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import ProductoModel

class ProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
               # Pasarle metadatos a la clase de la cual estamos heredando
                # model obtendra toda la configuracion del modelo y la pondra para cuestiones del serializador
        model = ProductoModel
        #para indicar que valida llaves fk
        include_fk = True