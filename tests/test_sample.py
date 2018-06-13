from pyds import array

import pytest

def test_case1():
    arr = array(10)
    assert arr._size == 10
