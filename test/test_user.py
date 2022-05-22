from models import *
from werkzeug.security import generate_password_hash, check_password_hash

def new_user():
    usname = "Test1"
    passwd = "test1"
    user = UserModel(usname, passwd)
    assert user.username == "Test1"
    assert check_password_hash(user.password,passwd)
    assert not check_password_hash(passwd,passwd)
