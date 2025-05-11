import numpy as np

def merge_sort(array):
    if len(array) > 1:
        div = len(array) // 2
        # array[:div] = de Zero até o valor de div
        left = array[:div].copy()

        # array[div:] = Do valor de div até o final do array
        right = array[div:].copy()
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Ordena esquerda e direita
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # ordenação final
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

print(merge_sort(np.array([15, 34, 8, 3])))


print(merge_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))

print(merge_sort(np.array([38, 27, 43, 3, 9, 82, 10])))