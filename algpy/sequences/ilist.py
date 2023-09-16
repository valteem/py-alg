# double linked list based on insert/remove operation

class IList():
    class Node():
        def __init__(self, elt, prev, next):
            self._elt = elt
            self._prev = prev
            self._next = next
    def __init__(self):
        self._size = 0
        self._head = self.Node(None, None, None)
        self._tail = self.Node(None, None, None)
        self._tail._next = self._head
        self._head._prev = self._tail
    def is_empty(self):
        return self._size == 0
    def head(self):
        return self._head
    def tail(self):
        return self._tail
    def insert(self, elt, prev, next):
        n = self.Node(elt, prev, next)
        prev._next = n
        next._prev = n
        self._size  += 1
        return n
    def remove(self, node):
        elt = node._elt
        prev = node._prev
        next = node._next
        prev._next = next
        next._prev = prev
        node._prev = node._next = node._elt = None
        self._size -= 1
        return elt
    def __str__(self):
        if self._size == 0:
            return "empty list"
        r = "tail<->"
        n = self._tail._next
        for i in range(self._size):
            r += str(n._elt) + "<->"
            n = n._next
        r += "head"
        return r