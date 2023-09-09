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
    
__left_delim__ = '{[('
__right_delim__ =  '}])'

def match_delim(expr) -> bool:
    s = Stack()
    for c in expr:
        if c in __left_delim__:
            s.push(c)
        elif c in __right_delim__:
            if s.is_empty():
                return False
            elif __right_delim__.index(c) != __left_delim__.index(s.pop()):
                return False
    return s.is_empty()