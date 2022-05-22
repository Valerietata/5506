from app import app
import config


def setup():
    app.config.from_object(config)
    app.config['TESTING'] = True
    app.config['DEBUG'] = True


def test_login_page(new_app):
    rv = new_app.get('http://localhost:5000/user/login')
    assert rv.status_code == 200
    assert b'<title>Login</title>' in rv.data


def test_register_page(new_app):
    rv = new_app.get('http://localhost:5000/user/register')
    assert rv.status_code == 200
    assert b'<title>Register</title>' in rv.data


def test_logout_page(new_app):
    rv = new_app.get('http://localhost:5000/user/logout')
    assert rv.status_code == 302
    assert rv.headers['Location'] == "http://localhost:5000/user/login"


def test_ranking_page(new_app):
    rv = new_app.get('http://localhost:5000/user/allranking')
    assert rv.status_code == 200
    assert b'<title>Ranking</title>' in rv.data


def test_intro_page(new_app):
    rv = new_app.get('http://localhost:5000/')
    assert rv.status_code == 200
    assert b'<title>Intro</title>' in rv.data


def test_play_page(new_app):
    rv = new_app.get('http://localhost:5000/play')
    assert rv.status_code == 302
    assert rv.headers['Location'] == "http://localhost:5000/user/login"


def login(new_app):
    """Login helper function"""
    with new_app.session_transaction() as sess:
        sess['user_id'] = 1


def test_play_logged_page(new_app):
    login(new_app)
    rv = new_app.get('http://localhost:5000/play')
    assert rv.status_code == 200


def test_rank_logged_page(new_app):
    login(new_app)
    rv = new_app.get('http://localhost:5000/user/showranking')
    assert rv.status_code == 200


def test_login(new_app):
    rv = new_app.post('http://localhost:5000/user/login', data=dict(username='hang', password='hang'))
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://localhost:5000/'


def test_register(new_app):
    rv = new_app.post('http://localhost:5000/user/register',
                      data=dict(username='Test1112', password='test111', password_confirm='test111'))
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://localhost:5000/user/login'
