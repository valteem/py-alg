from algpy.sequences.deque import CircularDeque
#from algpy import EmptyDeque
import pytest

def test_deque() -> None:
    
    q_cap = 5
    q = CircularDeque(q_cap)
    
    with pytest.raises(Exception) as exc:
        v = q.delete_first()
    assert str(exc.value) == "deque is empty"

    with pytest.raises(Exception) as exc:
        v = q.delete_last()
    assert str(exc.value) == "deque is empty"

    for k in range(q_cap):
        q.add_first(k)
        q.add_last(k)

    for k in range(q_cap):
        v = q.delete_first()
        assert v == q_cap - k - 1
        w = q.delete_last()
        assert w == q_cap - k - 1