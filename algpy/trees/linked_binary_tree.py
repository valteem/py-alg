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