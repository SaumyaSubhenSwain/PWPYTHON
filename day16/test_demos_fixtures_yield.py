# Fixture : Re-usable function

import pytest

@pytest.fixture
def setup():
    print("setup browser..")
    yield
    print("close browser..")

def test_one(setup):
    print("This is my test one")

def test_two(setup):
    print("This is my test two")

def test_three(setup):
    print("This is my test three")

def test_four(setup):
    print("This is my test Four")

