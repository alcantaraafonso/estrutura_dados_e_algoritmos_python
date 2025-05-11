import numpy as np

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


print(selection_sort(np.array([15, 34, 8, 3])))




print(selection_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))