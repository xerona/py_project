from models import Player
from schemas.player import PlayerSchema
from services.base import BaseService



class PlayerGETService(BaseService):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    @property
    def read_only(self):
        return [
            "first_name",
            "last_name",
        ]

    @property
    def read_schema(self):
        return PlayerSchema(only=self.read_only, session=self.session)

    def get(self):
        players = self.session.query(Player).all()
        return self.read_schema.dump(players, many=True)
        # return [{
        #     "first_name": "me",
        #     "last_name": "you"
        # }]
