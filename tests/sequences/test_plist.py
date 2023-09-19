from algpy import PList

import pytest

def test_pos():

    p = PList()
    p.insert_to_head("apples")
    u = p.head()
    v = p.head()

    assert u == v # works
#    assert u is v # error

def test_insert():

    p = PList()
    cabbage = p.insert_to_tail("cabbage")
    onion = p.insert_after("onion", cabbage)
    p.insert_before("potato", onion)

    assert p.__str__() == "tail<->cabbage<->potato<->onion<->head"


def test_access():

    p = PList()

    apple = p.insert_to_head("apple")
    assert p.head().elt() == "apple"

    cherry = p.insert_before("cherry", apple)
    assert p.before(apple).elt() == "cherry"

    p.insert_after("pear", cherry)
    assert p.before(apple).elt() == p.after(cherry).elt() == "pear"


def test_iter():

    p = PList()

    cap = 10

    for i in range(cap):
        if p.is_empty():
            c = p.insert_to_tail(i)
        else:
            c = p.insert_after(i, c)
    
    i = 0
    for e in p:
        assert e == i
        i += 1

def test_remove():
     
    p = PList()
     
    cap = 10

    r = [] # positions for removal

    for i in range(cap):
        pos = p.insert_to_head(i)
        if i % 2:
           r.append(pos) # adding even positions
    
    for v in r:
        p.remove(v) # removing even positions

    i = 0
    c = p.tail()
    while i < cap:
        assert c.elt() == i
        i += 2
        c = p.after(c)


def test_replace():

    p = PList()

    cap = 10

    for i in range(cap):
        p.insert_to_head(i)

    c = p.tail()
    for i in range(cap):
        p.replace(i * 2, c)
        c = p.after(c)

    c = p.tail()
    for i in range(cap):
        assert c.elt() == i * 2
        c = p.after(c)


    


            

      
    