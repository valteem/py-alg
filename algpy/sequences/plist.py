# Positional List ADT based on double linked list with insert/remove operations

from .ilist import IList

class PList(IList):
    class Position:
        def __init__(self, cont, node) -> None:
            self._cont = cont # 'container' - list to which this position belongs
            self._node = node
        def elt(self):
            return self._node.elt()
        def __eq__(self, other) -> bool:
            return type(other) is type(self) and other._node is self._node # 'is' used for identity, '==' for equality
        def __ne__(self, other) -> bool:
            return (self == other)
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
    def insert_between(self, elt, prev, next):
        node = super().insert(elt, prev, next)
        return self._position(node)
    def insert_to_head(self, elt):
        return self.insert_between(elt, self._head._prev, self._head)
    def head(self):
        return self._position(self._head._prev)