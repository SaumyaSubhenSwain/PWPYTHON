# Fixture : Re-usable function

# scope="function"  fixture will be called before every test function executes
# scope="module"   fixture will be called only once before test functions executes
# scope="class"   fixture will be called only once before the class
# scope="session"  fixture will be called only once for session


# module --> class --> methods
# module --> function


import pytest

@pytest.fixture
def setup(scope="module"):
    print("setup browser..")

def test_one(setup):
    print("this is my test one")

def test_two(setup):
    print("this is my test two")

def test_three(setup):
    print("this is my test three")

