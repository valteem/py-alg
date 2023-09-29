""" ABC for binary tree"""

from tree import Tree

from typing import Union
from collections.abc import Iterable

class BinaryTree(Tree):

    def left(self, pos: Tree.Position) -> Union[Tree.Position, None]:
        raise NotImplementedError("to be implemented by a subclass")
    
    def right(self, pos: Tree.Position) -> Union[Tree.Position, None]:
        raise NotImplementedError("to be implemented by a subclass")
    
    def sibling(self, pos: Tree.Position) -> Union[Tree.Position, None]:
        parent = self.parent(p)
        if parent is None: # position is binary tree root, hence its parent is None
            return None    # no siblings for root node
        else:
            if pos == self.left(parent):
                return self.right(parent)
            else:
                return self.right(parent)
            
    def children(self, pos: Tree.Position) -> Iterable[Tree.Position]:
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)