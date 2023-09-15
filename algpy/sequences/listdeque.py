from .dl_list import DoubleLinkedList

from typing import Any

class ListDeque():
    def __init__(self) -> None:
        self._list = DoubleLinkedList()
    def is_empty(self) -> bool:
        return self._list.is_empty()
    def add_first(self, element) -> None:
        self._list.add_to_head(element)
    def add_last(self, element) -> None:
        self._list.add_to_tail(element)
    def delete_first(self) -> Any:
        return self._list.remove_from_head()
    def delete_last(self) -> Any:
        return self._list.remove_from_tail()