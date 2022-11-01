from chapter01.chapter01 import reverse_array, insertion_sort


def test_reverse_array():
    assert (reverse_array([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1])
    assert (reverse_array([1, 2, 3, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1])
    assert (reverse_array([1, 2, 3, 1, 2, 3]) == [3, 2, 1, 3, 2, 1])


def test_insertion_sort():
    assert (insertion_sort([4, 6, 7, 5, 3, 7, 8]) == [3, 4, 5, 6, 7, 7, 8])
    assert (insertion_sort([9, 8, 7, 6, 5, 4, 3, 2]) == [2, 3, 4, 5, 6, 7, 8, 9])
