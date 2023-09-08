from algpy import Stack
from algpy import EmptyStack
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