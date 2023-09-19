from algpy import Stack
from algpy import EmptyStack
from algpy import match_delim
import pytest

def test_stack():
    
    s = Stack()
    
    with pytest.raises(Exception) as exc:
        e = s.top()
    assert str(exc.value) == "stack is empty"

    s.push("e1")
    assert s.top() == "e1"
    s.push("e2")
    assert s.top() == "e2"
    e = s.pop()
    assert e == "e2"
    assert s.top()  == "e1"

def test_match_delim():

    s1 = '{a+[b+(m+n)]}'
    assert match_delim(s1) == True
    s2 = '{a+[b+(m+n)]'
    assert match_delim(s2) == False