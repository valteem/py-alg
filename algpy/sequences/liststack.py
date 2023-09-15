from .dl_list import DoubleLinkedList
from typing import Any

class ListStack():
    def __init__(self) -> None:
        self._list = DoubleLinkedList()
    def is_empty(self) -> bool:
        return self._list.is_empty()
    def push(self, element: Any) -> None:
        self._list.add_to_head(element)
    def pop(self) -> Any:
        return self._list.remove_from_head()
    def __str__(self) -> str:
        if self._list.is_empty():
            return "empty stack"
        else:
            return self._list.__str__()