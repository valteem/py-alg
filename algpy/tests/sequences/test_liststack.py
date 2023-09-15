from algpy import ListStack

import pytest

def test_liststack():
    
    s = ListStack()

    assert s.is_empty() == True

    cap = 10

    for i in range(cap):
        s.push(i + 1)
    
    for i in range(cap):
        v = s.pop()
        assert v == cap - i

    v = s.pop()
    assert v == None