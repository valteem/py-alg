# double linked list

from typing import Any

class EmptyList(Exception):
    pass

class Node():
    def __init__(self, elt, prev, next) -> None:
        self._elt = elt
        self._prev = prev
        self._next = next
    def elt(self) -> Any:
        return self._elt
    def prev(self) -> Any:
        return self._prev
    def next(self) -> Any:
        return self._next
    def set_prev(self, prev) -> None:
        self._prev = prev
    def set_next(self, next) -> None:
        self._next = next

class DoubleLinkedList():
    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None
    def is_empty(self) -> bool:
        return self._size == 0
    def add_head(self, elt) -> None:
        if self.is_empty():
            n = Node(elt, None, None)
            self._head = n
            self._tail = n
        else:
            n = Node(elt, self._head, None)
            self._head.set_next(n)
            self._head = n
        self._size += 1

    def __str__(self) -> str:
        if self.is_empty():
            return "list empty"
        r = "head<->"
        n = self._head
        for i in range(self._size):
            r += str(self._size - i) + ":" + str(n.elt()) + "<->"
            n = n.prev()
        r += "tail"
        return r
    
l = DoubleLinkedList()
for v in range(5):
    l.add_head(v)
print(l)