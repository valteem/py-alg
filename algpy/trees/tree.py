# abstract base class

from __future__ import annotations
from collections.abc import Iterable

class Tree:

    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")
        def __eq__(self, other: Position) -> bool:
            raise NotImplementedError("must be implemented by subclass")
        def __ne__(self, other: Position) -> bool:
            return not (self == other)
        
    def root(self, pos) -> Position:
        raise NotImplementedError("must be implemented by subclass")
    
    def parent(self, pos: Position) -> Position:
        raise NotImplementedError("must be implemented by subclass")
    
    def num_of_children(self, pos: Position) -> int:
        raise NotImplementedError("must be implemented by subclass")
    
    def positions(self) -> Iterable[Position]:
        raise NotImplementedError("must be implemented by subclass")
    
    def children(self, pos: Position) -> Iterable[Position]:
        raise NotImplementedError("must be implemented by subclass")
    
    def __len__(self) -> int:
        raise NotImplementedError("must be implemented by subclass")
    
    def is_root(self, pos: Position) -> bool:
        return pos == self.root()
    
    def is_leaf(self, pos: Position) -> bool:
        return self.num_of_children(pos) == 0
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def depth(self, pos: Position) -> int:
        if self.is_root(pos):
            return 0
        else:
            return 1 + self.depth(self.parent(pos)) # recursive

    def _heigh1(self) -> int:
        """ O(n^2) worst case"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _heigh2(self, pos: Position) -> int:
        """ O(n) for a given subtree"""
        if self.is_leaf(pos):
            return 0
        else:
            return 1 + max(self._heigh2(c) for c in self.children(pos))
        
    def height(self, pos: Position = None) -> int:
        if pos == None:
            pos = self.root()
        return 1 + self._heigh2(pos)