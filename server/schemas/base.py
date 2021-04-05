import marshmallow as ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db


class BaseSchema(SQLAlchemyAutoSchema):

    class Meta:
        sqla_session = db.session
        include_relationships = True
        include_fk = True
        load_instance = True
        unknown = ma.EXCLUDE
