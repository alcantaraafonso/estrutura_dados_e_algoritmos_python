import numpy as np
import timeit
import random

def bubble_sort(array):
    #descobrir o tamanho do vetor
    n = len(array) 

    #percorrendo o vetor todo
    for i in range(n):
        """ o for j in range(0, n - i - 1) tem essa condição para que o
        for não pecorra por itens já ordenados, ou seja, os que estão
        mais à direita

        """ 
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # array[j + 1] = array[j]
                # array[j] = array[j - 1]

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

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

def shell_sort(array):

    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //=2 # interval = interval // 2
    return array

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

def selection_sort(array):
    n = len(array)
    # para percorrer todo o array
    for i in range(n):
        id_minimo_corrente = i
        """ é i + 1, assim não é necessário "olhar"para os elementos à esquerda
        que já estão ordenados
        """ 
        for j in range(i + 1, n):
            if array[id_minimo_corrente] > array[j]:
                id_minimo_corrente = j
        
        temp = array[i]
        array[i] = array[id_minimo_corrente]
        array[id_minimo_corrente] = temp

    return array

array = []
# array = np.random.rand(5000)
for _ in range(5000):
    array.append(round(random.random(), 4))

# array = np.array(array)

# tempo_bs = timeit.timeit(lambda: bubble_sort(array.copy()), number=1000)
# print(f"Tempo para bubble_sort: {tempo_bs:.6f} segundos")

tempo_q_s = timeit.timeit(lambda: quick_sort(array.copy(), 0, len(array) -1), number=1000)
print(f"Tempo para quick_sort: {tempo_q_s:.6f} segundos")

tempo_m_s = timeit.timeit(lambda: merge_sort(array.copy()), number=1000)
print(f"Tempo para merge_sort: {tempo_m_s:.6f} segundos")

tempo_s_s = timeit.timeit(lambda: shell_sort(array.copy()), number=1000)
print(f"Tempo para shell_sort: {tempo_s_s:.6f} segundos")

tempo_i_s = timeit.timeit(lambda: insertion_sort(array.copy()), number=1000)
print(f"Tempo para insertion_sort: {tempo_i_s:.6f} segundos")

tempo_sel_s = timeit.timeit(lambda: insertion_sort(array.copy()), number=1000)
print(f"Tempo para insertion_sort: {tempo_sel_s:.6f} segundos")