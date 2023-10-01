from __future__ import annotations
from typing import Any

from binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        """ https://wiki.python.org/moin/UsingSlots """
        __slots__ = '_elt', '_parent', '_left', '_right'
        def __init__(self, elt, parent = None, left = None, right = None) -> None:
            self._elt = elt
            self._parent = parent
            self._right = right
            self._left = left

    class Position(BinaryTree.Position):
        def __init__(self, cont: LinkedBinaryTree, node: _Node) -> None:
            self._cont = cont
            self._node = node
        def elt(self) -> Any:
            return self._node._elt
        def __eq__(self, other: Position) -> bool:
            return type(other) is type(self) and self._node is other._node
        """ __ne__() already defined in parent class """

    def _validate(self, pos: Position) -> _Node:
        if not isinstance(pos, self.Position):
            raise TypeError("pos should have Position type")
        if pos._cont is not self:
            raise ValueError("pos does not belong to this tree")
        if pos._node._parent is pos._node: # node parent is equal to node itself for deprecated nodes
            raise ValueError("position node is deprecated")
        return pos._node
    
    def _position(self, node: _Node) -> Position:
        return self.Position(node) if node is not None else None # return ... if ... else

    def __init__(self) -> None:
        self._root = None # new tree alway has None as root, it is replaced further on with _add_root()
        self._size = 0

    def __len__(self) -> int:
        return self._size
    
    def root(self) -> Position:
        return self.Position(self._root)
    
    def parent(self, pos: Position) -> Position:
        return self._position(self._validate(pos)._parent)
    
    def left(self, pos: Position) -> Position:
        return self._position(self._validate(pos)._left)
    
    def right(self, pos: Position) -> Position:
        return self._position(self._validate(pos)._right)
    
    def num_of_children(self, pos: Position) -> int:
        node = self._validate(pos)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count