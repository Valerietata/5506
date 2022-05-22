import os
import tempfile

import pytest
from app import app
from models import *

@pytest.fixture
def new_user():
    user = UserModel("Test1", "test1")
    return user


@pytest.fixture
def new_app():
    # app, migrate = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    with app.test_client() as client:
        yield client
