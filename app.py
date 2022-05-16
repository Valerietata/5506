"""
CITS5507 Project2
"""
from flask import Flask
from flask_migrate import Migrate
from models import *

import config
from exts import db

from blueprints import game_bp
from blueprints import user_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(game_bp)
app.register_blueprint(user_bp)

# db.create_all()


if __name__ == '__main__':
    app.run()
