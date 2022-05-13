"""
CITS5507 Project2
"""
from flask import Flask
import config
from exts import db
from blueprints import game_bp
from blueprints import user_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(game_bp)
app.register_blueprint(user_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
