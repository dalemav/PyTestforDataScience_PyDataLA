"""
A module that tests the add() function from adder.py

"""

import adder

def test_add_positive_int():
    """Test add() for positive integers 2 and 10"""
    number = adder.add(2, 10)
    assert number == 12

def test_add_negative_int():
    """Test add() for negative integers -7 and -3"""
    number = adder.add(-7, -3)
    assert number == -10
