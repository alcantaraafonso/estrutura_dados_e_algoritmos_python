import timeit

def lista1():
    """
    Objetivo é criar uma lista com 1000 elementos
    """
    lista = []
    for i in range(1000):
        lista += [i]
    return lista	    

print("Testando a função lista1")
print(lista1())

def testar_big_o_lista1():
    """
    Testa a complexidade de tempo da função lista1 com diferentes tamanhos de entrada.
    """
    tempo = timeit.timeit(lambda: lista1(), number=10)
    print(f"Tempo de execução: {tempo:.6f} segundos")

print("\nAnalisando o Big-O da função lista1:")
testar_big_o_lista1()

def lista2():
    return range(1000)

print("Testando a função lista2")
l = lista2()
print(l)

def testar_big_o_lista2():
    """
    Testa a complexidade de tempo da função lista1 com diferentes tamanhos de entrada.
    """
    tempo = timeit.timeit(lambda: lista2(), number=10)
    print(f"Tempo de execução: {tempo:.6f} segundos")

print("\nAnalisando o Big-O da função lista2:")
testar_big_o_lista2()