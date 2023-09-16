from algpy import PList

import pytest

def test_plist():

    p = PList()
    p.insert_to_head("apples")
    u = p.head()
    v = p.head()

    assert u == v # works
#    assert u is v # error