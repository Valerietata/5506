from flask import Blueprint, render_template
from decorators import login_required

bp = Blueprint("game", __name__, url_prefix="")


@bp.route("/play")
@login_required
def play():
    return render_template('game_play.html')


@bp.route("/")
def intro():
    return render_template('intro.html')

