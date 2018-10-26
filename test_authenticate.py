import authenticate
import sys
import pytest


# valid usernames and passwords
@pytest.mark.parametrize("username, password", [
    ("mouse", "fjueurk"),
    ("cat", "fjuejek13837"),
    ("bounce", "epwnnru197"),
])
def test_successLoginUser(username, password):
    result = authenticate.loginUser(username, password)

    assert result == True


# invalid usernames and passwords
@pytest.mark.parametrize("username, password", [
    ("mouse", "123flower"),
    ("cat", "Water1983"),
    ("bounce", "123"),
    ("bounce", "snow"),
])
def test_failLoginUser(username, password):
    result = authenticate.loginUser(username, password)

    assert result == False