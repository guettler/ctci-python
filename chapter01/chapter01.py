from typing import List


def reverse_array(array: List[int]):
    for i in range(0, round(len(array)/2)):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp

    return array


def insertion_sort(array: List[int]):
    for i in range(0, len(array)):
        value_to_sort = array[i]
        j = i
        while j > 0 and array[j-1] > value_to_sort:
            array[j] = array[j-1]
            j -= 1
        array[j] = value_to_sort
    return array



