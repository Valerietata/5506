def test_new_user_with_fixture(new_user):
    assert new_user.username == "Test1"
    assert new_user.password != "test1"