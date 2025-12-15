# Fixture : Re-usable function

import pytest

@pytest.fixture
def setup():
    print("setup browser..")
    return "chrome"

def test_one(setup):
    print("this is my test one")
    print("Browser is:",setup)


def test_two(setup):
    print("this is my test two")
    print("Browser is:", setup)

def test_three(setup):
    print("this is my test three")
    print("Browser is:", setup)

