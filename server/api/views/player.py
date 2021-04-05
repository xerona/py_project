from flask import jsonify
from flask_login import login_required
from flask.views import MethodView

from api.base import api
from services.player import PlayerGETService


class PlayerView(MethodView):

    decorators = [login_required]

    def get(self):
        service = PlayerGETService()
        data = service.get()
        return jsonify(data)


player_view = PlayerView.as_view("player")
api.add_url_rule(
    "/player",
    methods=("GET",),
    view_func=player_view,
)
