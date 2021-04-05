import sqlalchemy as sa
from flask import current_app


class BaseService:
    def __init__(self, _session=None, **kwargs):
        self._session = _session

    @property
    def session(self):
        if self._session is None:
            from app import db

            self._session = db.session
        return self._session

    @property
    def app(self):
        return current_app
