from algpy import DoubleLinkedList
import pytest

def test_dl_list():

    t = 5

    l = DoubleLinkedList()

    for i in range(t):
        l.add_to_head(i)
        l.add_to_tail(i)
    
    s = l.__str__()
    assert s == "head<->10:4<->9:3<->8:2<->7:1<->6:0<->5:0<->4:1<->3:2<->2:3<->1:4<->tail"

    for i in range(t):
        u = l.remove_from_head()
        assert u == t - i - 1
        v = l.remove_from_tail()
        assert v == t - i - 1