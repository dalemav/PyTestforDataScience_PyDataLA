"""Add tests for adders here """
import pytest
from .. import my_module

@pytest.fixture(scope="session")
def adder_fixture():
    """Adder fixture function"""
    fixture_object = my_module.SingleObject(1)
    return fixture_object

def test_add_more_5(adder_fixture):
    """Test add_more 5"""
    result = adder_fixture.add_more(5)
    assert result == 6

def test_add_more_7(adder_fixture):
    """Test add_more 7"""
    result = adder_fixture.add_more(7)
    assert result == 8

def test_add_more_10(adder_fixture):
    """Test add_more 10"""
    result = adder_fixture.add_more(10)
    assert result == 11
