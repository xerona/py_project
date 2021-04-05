from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from api import baseapi
from config import Config


db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)


app = create_app(Config)
from views import *
app.register_blueprint(baseapi, url_prefix="/api")
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    from models.user import User
    return db.session.query(User).filter(User.id == userid).one()

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
