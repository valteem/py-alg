from algpy import PList
from algpy import ins_sort_plist

import pytest

def test_ins_sort_plist():
    pl = PList()
    unsorted_list = ["apple", "onion", "cherry", "berry", "plum", "pear"]
    for v in range(unsorted_list):
        pl.insert_to_head(v)
    ins_sort_plist(pl)
    sorted_list = []
    pos = pl.tail
    elt = pos.elt
    while elt != None:
        sorted_list.append(elt)
        pos = pl.after(pos)
        elt = pos.elt
    sorted_list_expected = ["apple", "berry", "cherry", "onion", "pear", "plum"]
    assert sorted_list == sorted_list_expected

