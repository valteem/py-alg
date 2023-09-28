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
    def children(self) -> Iterable[Position]:
        raise NotImplementedError("must be implemented by subclass")
    def __len__(self) -> int:
        raise NotImplementedError("must be implemented by subclass")
    def is_root(self, pos: Position) -> bool:
        return pos == self.root()
    def is_leaf(self, pos: Position) -> bool:
        return self.num_of_children(pos) == 0
    def is_empty(self) -> bool:
        return len(self) == 0
    