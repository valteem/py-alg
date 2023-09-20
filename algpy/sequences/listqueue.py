from algpy.sequences.dl_list import DoubleLinkedList

from typing import Any

class ListQueue():
    def __init__(self) -> None:
        self._list = DoubleLinkedList()
    def is_empty(self) -> bool:
        return self._list.is_empty()
    def enqueue(self, element: Any) -> None:
        self._list.add_to_tail(element)
    def dequeue(self) -> Any:
        return self._list.remove_from_head()