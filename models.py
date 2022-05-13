from datetime import datetime

from exts import db


class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, default="1234")
    joint_time = db.Column(db.DateTime, default=datetime.now)


class Ranking(db.Model):
    __tablename__ = "ranking"
    rank_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rank_user = db.Column(db.Integer, db.ForeignKey('user.uid'))
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, default="1234")
    joint_time = db.Column(db.DateTime, default=datetime.now)




class Article(db.Model):
    __tablename__ = "article"
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 外键是数据库层面的，不推荐在ORM中使用
    author_id = db.Column(db.Integer, db.ForeignKey("user.uid"))
    author = db.relationship("User", backref="articles")


class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False, default="1234")


class UserExtension(db.Model):
    __tablename__ = "user_extension"
    ueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    # db.backref
    # 1.在反向引用的时候，如果需要传递其他的一些参数，那么就需要用到这个参数,否则就不需要；只需要在relationship的backref上设置反向引用的名称即可
    # 2.userlist=False 代表反向引用的时候是一个对象，而不是一个列表
    user = db.relationship("User", backref=db.backref("extension", uselist=False))