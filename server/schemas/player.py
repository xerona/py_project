from models import Player
from schemas.base import BaseSchema


class PlayerSchema(BaseSchema):

    class Meta(BaseSchema.Meta):
        model = Player
