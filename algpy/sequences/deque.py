from typing import Any

class EmptyDeque(Exception):
    pass

class CircularDeque():
    def __init__(self, cap) -> None:
        self._arr = [None] * cap
        self._cap = cap
        self._front = 0
        self._size = 0
    def is_empty(self) -> bool:
        return self._size == 0
    def is_full(self) -> bool:
        return self._size == self._cap
    def _resize(self) -> None:
        new = [None] * 2 * self._cap
        i = self._front
        for k in range(self._size):
            new[k] = self._arr[i]
            i = (i + 1) % self._cap
        self._arr = new
        self._cap = 2 * self._cap
        self._front = 0
    def add_first(self, e) -> None:
        if self.is_full():
            self._resize()
        self._front = (self._front - 1) % self._cap
        self._arr[self._front] = e
        self._size += 1
    def delete_first(self) -> Any:
        if self.is_empty():
            raise EmptyDeque("deque is empty")
        r = self._arr[self._front]
        self._arr[self._front] = None
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return r
    def add_last(self, e) -> None:
        if self.is_full():
            self._resize()
        i = (self._front + self._size) % self._cap
        self._arr[i] = e
        self._size += 1
    def delete_last(self) -> Any:
        if self.is_empty():
            raise EmptyDeque("deque is empty")
        i = (self._front + self._size - 1) % self._cap
        r = self._arr[i]
        self._arr[i] = None
        self._size -= 1
        return r
    def __str__(self) -> str:
        if self.is_empty():
            return "empty deque"
        r = "first<-"
        i = self._front
        for k in range(self._size):
            r += + self._arr[i]
            i = (i + 1) % self._cap
        r += "<-last"
        return r