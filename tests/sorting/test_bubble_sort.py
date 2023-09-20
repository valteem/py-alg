from algpy.sorting.bubble_sort import bubble_sort

def test_bubble_sort():
    a = list("28657814")
    bubble_sort(a)
    assert a == list("12456788")