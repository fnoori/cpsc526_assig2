import enroll
import sys
import pytest

# good password
# the password is not [num][word] or [word][num]
# this test is checking to ensure the password being provided
#  conforms to the password requirements
@pytest.mark.parametrize("password", [
    ("fuj-ehd"),
    ("io'fk"),
    ("ryiec`837"),
    ("gjfin]"),
])  
def test_goodPassword(password):
    result = enroll.checkPassword(password)
    assert result == True


# bad password
# [number][word]
# this test is checking if there are english words
#  following a number, this ensures the [num][word]
#  is not being used
# this does not allow the user to use "simple" passwords,
#  making the user vulnerable to dictionary attacks 
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


# bad password
# [word][number]
# this test is checking if there are english words
#  before a number, this ensures the [word][num]
#  is not being used
# this does not allow the user to use "simple" passwords,
#  making the user vulnerable to dictionary attacks 
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


# bad password
# [word]
# this does not allow the user to use "simple" passwords,
#  making the user vulnerable to dictionary attacks 
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


# bad password
# [number]
# this does not allow the user to use "simple" passwords,
#  making the user vulnerable to dictionary attacks 
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


# check if string is word
# return true if input is a word
# this ensures the user is not using an English
#  dictionary word in their password, which would
#  make their account vulnerable to dictionary attack
@pytest.mark.parametrize("input", [
    ("Internet"),
    ("of"),
    ("Things"),
])
def test_realEnglishWord(input):
    result = enroll.isWord(input)

    assert result == True


# check if string is not a word
# return true if input is not a word
# makes sure the input is not an English dictionary word
#  aides in preventing dictionary attacks
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
# this tests to ensure the account creation is working accordingly with correct
#  username/password requirements
@pytest.mark.parametrize("username, password", [
    ("mouse", "fjueurk"),
    ("cat", "fjuejek13837"),
    ("bounce", "epwnnru197"),
])
def test_successfulCompleteUserCreation(username, password):
    alreadyExistsResult = enroll.userAlreadyExists(username)
    result = enroll.accepted(username, password)

    assert result == None


# create user with incorrect password
# user will not be granted access'
# this ensures that if an invalid password is provided, the user cannot create their
#  account, until they change their password to meet the requirements
@pytest.mark.parametrize("username, password", [
    ("mouse", "123flower"),
    ("cat", "Water1983"),
    ("bounce", "123"),
    ("bounce", "snow"),
])
def test_failedCompleteUserCreation(username, password):
    with pytest.raises(SystemExit) as sysExit:
        alreadyExistsResult = enroll.userAlreadyExists(username)
        passwordResult = enroll.checkPassword(password)
        result = enroll.accepted(username, password)

        assert sysExit.type == SystemExit
        assert sysExit.value.code == -1
