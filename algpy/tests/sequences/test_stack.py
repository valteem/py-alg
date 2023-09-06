from algpy import Stack
from algpy import EmptyStack

def test_stack():
    s = Stack()
    try:
        e = s.top()
    except EmptyStack:
        print("empty stack")