
# pytest is the module that provides us with testing helper functions.
# Mostly not needed initially, but you'll call on it in some cases.
# See documentation on pytest.
import pytest

# Import the module whose procedures and functions you want to test here.
import pyls

# Note that the procedures below that are testing for things **must**
# have their names start with "test_" ... just as this file's name
# also starts with "test_". `pytest` will automatically pick up
# such functions and run them when you run `uvx pytest` from the
# command line.
def test_dummy():
    """
    A sample dummy test for illustration. This test will always succeed.
    """
    assert 2 == 2, "Two and two must be the same"

def test_dummy_fails():
    """
    A sample dummy test for illustration. This test will always fail.
    """
    assert 2 == 2, "Two and three must be the same. (Really?)"



