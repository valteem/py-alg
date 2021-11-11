def binary_search(list_search, value_search, low, high):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if list_search[middle] ==  value_search:
            return True
        else:
            if value_search < list_search[middle]:
                return binary_search(list_search, value_search, low, middle - 1)
            else:
                return binary_search(list_search, value_search, middle + 1, high)