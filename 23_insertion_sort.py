import numpy as np

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        marked_element = array[i]
        j = i - 1
        while j >= 0 and marked_element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marked_element

    return array


print(insertion_sort(np.array([15, 34, 8, 3])))




print(insertion_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))