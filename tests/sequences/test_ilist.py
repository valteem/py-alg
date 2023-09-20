from algpy.sequences.ilist import IList

import pytest

def test_insert_between():

    l = IList()

    h = l.insert("apple", l.tail(), l.head())
    t = l.insert("onion", l.tail(), h)
    m = l.insert("nuts", t, h)
    assert l.__str__() == "tail<->onion<->nuts<->apple<->head"

    l.remove(m)
    assert l.__str__() == "tail<->onion<->apple<->head"

    l.remove(t)
    assert l.__str__() == "tail<->apple<->head"

    l.remove(h)
    assert l.__str__() == "empty list"