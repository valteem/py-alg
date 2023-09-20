# Positional List ADT based on double linked list with insert/remove operations

from algpy.sequences.ilist import IList

class PList(IList):

    class Position:
        def __init__(self, cont, node) -> None:
            self._cont = cont # 'container' - list to which this position belongs
            self._node = node
        def elt(self):
            return self._node._elt
        def __eq__(self, other) -> bool:
            return type(other) is type(self) and other._node is self._node # 'is' used for identity, '==' for equality
        def __ne__(self, other) -> bool:
            return not (self == other)
        
    def _validate(self, pos):
        if not isinstance(pos, self.Position):
            raise TypeError("pos must be of type Position")
        if pos._cont is not self:
            raise ValueError("pos does not belong to this list  ")
        if pos._node._next == None:
            raise ValueError("pos is removed") # underlying IList setx _next and _prev to None for removed nodes 
        return pos._node
    
    def _position(self, node):
        if node is self._head or node is self._tail:
            return None
        return self.Position(self, node)
    
    # access to nodes via their positions in list
    def head(self):
        return self._position(self._head._prev)
    def tail(self):
        return self._position(self._tail._next)
    def after(self, pos):
        n = self._validate(pos)
        return self._position(n._next)
    def before(self, pos):
        n = self._validate(pos)
        return self._position(n._prev)
    def __iter__(self):
        c = self.tail()        # cursor (position)
        while c is not None:   # reaching head sentinel
            yield c.elt()      # return value to caller functions, wait for next call at the same place
            c = self.after(c)
    
    # adding nodes to list, return position of added nodes
    def insert_between(self, elt, prev, next):
        node = super().insert(elt, prev, next)
        return self._position(node)
    def insert_to_head(self, elt):
        return self.insert_between(elt, self._head._prev, self._head)
    def insert_to_tail(self, elt):
        return self.insert_between(elt, self._tail, self._tail._next)
    def insert_before(self, elt, pos):
        n = self._validate(pos)
        return self.insert_between(elt, n._prev, n)
    def insert_after(self, elt, pos):
        n = self._validate(pos)
        return self.insert_between(elt, n, n._next)
    
    # removal, replacement - returning node values (elements)
    def remove(self, pos):
        n = self._validate(pos)
        return super().remove(n) #inherited IList remove() method
    def replace(self, elt, pos):
        n = self._validate(pos)
        r = n._elt
        n._elt = elt
        return r