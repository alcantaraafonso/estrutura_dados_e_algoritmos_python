import numpy as np

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

print(bubble_sort(np.array([15, 34, 8, 3])))




print(bubble_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))