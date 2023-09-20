from algpy.sequences.plist import PList
from algpy.sorting.ins_sort_plist import ins_sort_plist

import pytest

def test_ins_sort_plist():
    pl = PList()
    unsorted_list = ["apple", "onion", "cherry", "berry", "plum", "pear"]
    for v in unsorted_list:
        pl.insert_to_head(v)
    ins_sort_plist(pl)
    sorted_list = []
    pos = pl.tail()   
    for k in range(pl._size): #TODO: replace logic with hidden attribute _size
        elt = pos.elt()
        sorted_list.append(elt)
        pos = pl.after(pos)
    sorted_list_expected = ["apple", "berry", "cherry", "onion", "pear", "plum"]
    assert sorted_list == sorted_list_expected

