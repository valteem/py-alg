from algpy.sequences.queue import CircularQueue, EmptyQueue

import pytest

def test_queue():

    q_cap = 5
    q = CircularQueue(q_cap)

    with pytest.raises(Exception) as exc:
        v = q.dequeue()
    assert str(exc.value) == "queue is empty"

    for k in range(q_cap):
        q.enqueue(k)

    for k in range(q_cap):
        v = q.dequeue()
        assert v == k

def test_queue_resize():
    
    q_cap_init = 5
    q = CircularQueue(q_cap_init)

    for k in range(q_cap_init * 2):
        q.enqueue(k)

    for k in range(q_cap_init * 2):
        v = q.dequeue()
        assert v == k