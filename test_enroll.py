import enroll
import sys
import pytest

'''
# good password
# should pass
@pytest.mark.parametrize("password", [
    ("fuj-ehd"),
    ("io'fk"),
    ("ryiec`837"),
    ("gjfin]"),
])  
def test_goodPassword(password):
    result = enroll.checkPassword(password)
    assert result == True


# [number][word]
# should fail
@pytest.mark.parametrize("password", [
    ("1239ice"),
    ("8.01table"),
    ("6.19get"),
])  
def test_badNumWordPassword(password):
    # since on fail, sys.exit() is called
    with pytest.raises(SystemExit) as sysExit:
        result = enroll.checkPassword(password)

        # check for both exit type and exit code
        assert sysExit.type == SystemExit
        assert sysExit.value.code == -1


# [word][number]     
@pytest.mark.parametrize("password", [
    ("mouse123"),
    ("guard1.20"),
    ("phone20.01"),
])  
def test_badWordNumPassword(password):
    # since on fail, sys.exit() is called
    with pytest.raises(SystemExit) as sysExit:
        result = enroll.checkPassword(password)

        # check for both exit type and exit code
        assert sysExit.type == SystemExit
        assert sysExit.value.code == -1


# [word]
# should fail
@pytest.mark.parametrize("password", [
    ("Hey"),
    ("Edward"),
    ("How"),
    ("Is"),
    ("It"),
    ("Going"),
])
def test_wordPassword(password):
    # since on fail, sys.exit() is called
    with pytest.raises(SystemExit) as sysExit:
        result = enroll.checkPassword(password)

        # check for both exit type and exit code
        assert sysExit.type == SystemExit
        assert sysExit.value.code == -1


# [number]
# should fail
@pytest.mark.parametrize("password", [
    ("123"),
    ("9723"),
    ("123382748273498"),
    ("1.2937338"),
])  
def test_numberPassword(password):
    # since on fail, sys.exit() is called
    with pytest.raises(SystemExit) as sysExit:
        result = enroll.checkPassword(password)

        # check for both exit type and exit code
        assert sysExit.type == SystemExit
        assert sysExit.value.code == -1


# see if string is word
# return true if input is a word
@pytest.mark.parametrize("input", [
    ("Internet"),
    ("of"),
    ("Things"),
])
def test_realEnglishWord(input):
    result = enroll.isWord(input)

    assert result == True


# see if string is word
# return true if input is not a word
@pytest.mark.parametrize("input", [
    ("asfiue"),
    ("aerfnf"),
    ("sfufmfkdooo"),
])
def test_fakeWord(input):
    result = enroll.isWord(input)
    assert result == False    


# create user with correct username/password
# when this test finishes, new users with the ones specified are added to the credentials.json file
# should pass
@pytest.mark.parametrize("username, password", [
    ("mouse", "fjueurk"),
    ("cat", "fjuejek13837"),
    ("bounce", "epwnnru197"),
])
def test_successfulCompleteUserCreation(username, password):
    alreadyExistsResult = enroll.userAlreadyExists(username)
    result = enroll.accepted(username, password)

    assert result == None
'''


@pytest.mark.parametrize("username, password", [
    ("mouse", "123flower"),
    ("cat", "Water1983"),
    ("bounce", "123"),
    ("bounce", "snow"),
])
def test_failedCompleteUserCreation(username, password):
    alreadyExistsResult = enroll.userAlreadyExists(username)
    result = enroll.accepted(username, password)

    assert result == None



