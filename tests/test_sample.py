import core

import pytest

def test_case1():
    obj = core.module.test1()
    assert obj.test_fn() == 90

def test_case2():
    obj = core.module.test1()
    assert obj.test_fn2() == 100