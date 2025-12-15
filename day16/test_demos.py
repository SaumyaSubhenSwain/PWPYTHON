import pytest


def test_one():
    print("This is my test one")

def test_two():
    print("This is my test two")

def test_three():
    print("This is my test three")


# class TestClass:
#     def test_one(self):
#         print("this is my test one")
#
#     def test_two(self):
#         print("this is my test two")
#
#     def test_three(self):
#         print("this is my test three")


'''
To run all the tests in the module
    pytest test_demos.py
    pytest test_demos.py -s
    pytest test_demos.py -s -v

To run specific test in the module
    pytest test_demos.py::test_one -s -v
    pytest test_demos.py::test_two -s -v
    pytest test_demos.py::test_three -s -v

-s  : you can see all print() outputs live in the console while the test runs.
-v :  Runs pytest in verbose mode. Shows detailed test execution information.

'''