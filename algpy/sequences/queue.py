class EmptyQueue(Exception):
    pass

class CircularQueue():
    def __init__(self, cap) -> None:
        self._arr = [None] * cap # ([] * cap) returns empty list with zero length
        self._cap = cap
        self._size = 0
        self._front = 0
    def is_empty(self) -> bool:
        return self._size == 0
    def is_full(self) -> bool:
        self._size == self._cap
    def _resize(self):
        new = [None] * 2 * self._cap
        i = self._front
        for k in range (self._size):
            new[k] = self._arr[i]
            i = (i + 1) % self._cap
        self._arr = new
        self._cap = self._cap * 2
        self._front = 0
    def enqueue(self, e):
        if self._size == self._cap:
            self._resize()
        i = (self._front + self._size) % self._cap
        self._arr[i] = e
        self._size += 1
    def dequeue(self):
        if self._size == 0:
            raise EmptyQueue("queue is empty")
        r = self._arr[self._front]
        self._arr[self._front] = None #enable GC
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return r