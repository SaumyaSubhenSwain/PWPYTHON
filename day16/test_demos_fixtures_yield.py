# Fixture : Re-usable function

import pytest

@pytest.fixture
def setup():
    print("setup browser..")
    yield
    print("close browser..")

def test_one(setup):
    print("this is my test one")

def test_two(setup):
    print("this is my test two")

def test_three(setup):
    print("this is my test three")

def test_four(setup):
    print("this is my test four")

