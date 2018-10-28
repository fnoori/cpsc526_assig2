import authenticate
import sys
import pytest


# ideal scenario
# valid usernames and passwords
# if a correct username/password combination is provided
#  the user is given access to the system
@pytest.mark.parametrize("username, password", [
    ("mouse", "fjueurk"),
    ("cat", "fjuejek13837"),
    ("bounce", "epwnnru197"),
])
def test_successLoginUser(username, password):
    result = authenticate.loginUser(username, password)

    assert result == True


# bad scenario
# invalid usernames and passwords
# if an invalid username/password is given, the system
#  will not allow the individual to login
@pytest.mark.parametrize("username, password", [
    ("mouse", "123flower"),
    ("cat", "Water1983"),
    ("bounce", "123"),
    ("bounce", "snow"),
])
def test_failLoginUser(username, password):
    result = authenticate.loginUser(username, password)

    assert result == False