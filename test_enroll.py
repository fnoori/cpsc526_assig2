import enroll
import sys
import pytest

@pytest.mark.goodPassword
def test_checkPassword():
    result = enroll.checkPassword("asdffj")
    assert result == True