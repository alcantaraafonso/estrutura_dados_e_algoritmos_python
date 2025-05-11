import numpy as np

def partition(array, init, ending):
    pivot = array[ending]
    i = init - 1

    for j in range(init, ending):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[ending] = array[ending], array[i + 1]
    return i + 1

def quick_sort(array, init, ending):
    if init < ending:
        position = partition(array, init, ending)

        # esquerda
        quick_sort(array, init, position - 1)

        #direira
        quick_sort(array, position + 1, ending)

    return array

array_1 = np.array([15, 34, 8, 3])
print(quick_sort(array_1, 0, len(array_1) -1))

array_2 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(quick_sort(array_2, 0, len(array_2) -1))

array_3 = np.array([38, 27, 43, 3, 9, 82, 10])
print(quick_sort(array_3, 0, len(array_3) -1))