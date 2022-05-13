from flask import Blueprint, render_template

bp = Blueprint("game", __name__, url_prefix="")


@bp.route("/play")
def play():
    return render_template('game_play.html')


@bp.route("/")
def intro():
    return render_template('intro.html')


@bp.route("/tips")
def tips():
    return render_template('tips.html')
