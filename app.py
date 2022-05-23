"""
CITS5507 Project2
"""
from flask import Flask, g, session, render_template
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

@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # setattr(g, "user", user)
            g.user = user
        except:
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


@app.errorhandler(404)
def page_unauthorized(error):
    return render_template('404.html', error_info=error), 404

if __name__ == '__main__':
    app.run()
