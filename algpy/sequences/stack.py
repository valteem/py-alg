class EmptyStack(Exception):
    pass

class Stack:
    def __init__(self) -> None:
        self._arr = []
    def is_empty(self) -> bool:
        return len(self._arr) == 0
    def top(self):
        if self.is_empty():
            raise EmptyStack("stack is empty")
        return self._arr[-1]
    def push(self, e) -> None:
        self._arr.append(e)
    def pop(self) -> any:
            if self.is_empty():
                raise EmptyStack("stack is empty")
            return self._arr.pop()