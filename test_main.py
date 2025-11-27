"""tests"""
from main import add


def test_add_normal():
    """test for adding"""
    assert add(3, 4) == 7
