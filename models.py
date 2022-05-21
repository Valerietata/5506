from exts import db


class UserModel(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, default="1234")


class RankingModel(db.Model):
    __tablename__ = "ranking"
    rank_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rank_user = db.Column(db.String(200), db.ForeignKey('user.username'))
    wrong_moves = db.Column(db.Integer, nullable=False)
