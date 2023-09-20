from algpy.sequences.listqueue import ListQueue

import pytest

def test_listqueue():

    q = ListQueue()

    assert q.is_empty() == True

    cap = 10

    for i in range(cap):
        q.enqueue(i)
    
    for i in range(cap):
        v = q.dequeue()
        assert v == i

    assert q.dequeue() == None