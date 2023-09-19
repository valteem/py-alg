from algpy import ListDeque

import pytest

def test_listdeque():

    q = ListDeque()

    assert q.is_empty() == True

    cap = 5

    for i in range(cap):
        q.add_first(i + 1)
        q.add_last(i + 1)
    
    assert q._list._size == 2 * cap

    for i in range(cap):
        assert q.delete_first() == cap - i
        assert q.delete_last() == cap - i

    assert q.delete_first() == None
    assert q.delete_last() == None